import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {execFileSync} from 'node:child_process';
const root=process.cwd();
const moduleNumber=Number(process.argv[2]||1);
const moduleName=moduleNumber===1?'01-introduction-to-r':'02-data-and-descriptive-statistics';
const runtime='/home/me/.cache/codex-runtimes/codex-primary-runtime/dependencies';
process.env.RUNTIME_NODE_MODULES=path.join(runtime,'node/node_modules');
const {Presentation,PresentationFile}=await import(pathToFileURL(path.join(process.env.RUNTIME_NODE_MODULES,'@oai/artifact-tool/dist/artifact_tool.mjs')).href);
const skill='/home/me/.codex/plugins/cache/openai-primary-runtime/presentations/26.1022.11436/skills/presentations';
const out=path.join(root,'20261/_output/teaching-slides');
const build=path.join(root,`20261/_output/.module${String(moduleNumber).padStart(2,'0')}-teaching-build`);
const data=JSON.parse(await fs.readFile(path.join(build,'layouts.json'),'utf8'));
const deck=Presentation.create({slideSize:{width:1600,height:900}});
const faces={sans:'DejaVu Sans',bold:'DejaVu Sans',mono:'DejaVu Sans Mono'};
const tables=[];
for(const s of data){
  const slide=deck.slides.add();
  slide.background.fill=s.kind==='divider'?'#F5EDF4':'#FFFFFF';
  for(const b of s.boxes){
    const box=slide.shapes.add({geometry:'textbox',name:b.rtl?'case-narration-ar':undefined,position:{left:b.x,top:b.y,width:b.w,height:b.h},fill:'none',line:{fill:'none',width:0}});
    box.text=b.text;
    box.text.style={typeface:faces[b.face],fontSize:b.size,bold:b.face==='bold',color:b.color,insets:0,autoFit:'none',wrap:'none',alignment:b.rtl?'right':'left'};
  }
  if(s.image_layout){
    const f=s.image_layout;
    let file=path.join(root,f.path);
    if(file.endsWith('.gif')){
      // Use an extracted original animation frame; the Quarto animation remains linked.
      file=path.join(build,'grammar-frame.png');
    }
    const bytes=await fs.readFile(file);
    slide.images.add({blob:bytes.buffer.slice(bytes.byteOffset,bytes.byteOffset+bytes.byteLength),contentType:'image/png',alt:s.title,position:{left:f.x,top:f.y,width:f.w,height:f.h},fit:'contain'});
  }
  if(s.table_layout){
    tables.push(s.number);
    const f=s.table_layout;
    const values=s.table||[['Patient ID','Height (cm)','Weight (kg)','Systolic (mmHg)','Diastolic (mmHg)'],['10200','165','71','120','80'],['3600','180','92','110','85'],['8437','172','76','118','82'],['5911','167','82','115','78']];
    const table=slide.tables.add({rows:values.length,columns:values[0].length,left:f.x,top:f.y,width:f.w,height:f.h,columnWidths:s.table?values[0].map(()=>f.w/values[0].length):[230,260,260,345,345],values});
    table.borders.assign({fill:'#DEE2E6',width:1,style:'solid'});
    for(let r=0;r<values.length;r++)for(let c=0;c<values[0].length;c++){
      const cell=table.getCell(r,c);cell.fill=r===0?'#F3F4F6':'#FFFFFF';
      cell.text.style={typeface:'DejaVu Sans',fontSize:s.table?26:(r===0?26:30),color:'#2F343B',bold:r===0,insets:10,alignment:'left',wrap:'square'};
    }
  }
  slide.speakerNotes.text=`Source: 20261/modules/${moduleName}/${s.source}, lines ${s.start}-${s.end}, section ${s.heading}.\n${s.code_chunk?"R example source chunk: "+s.code_chunk+".\n":""}${s.refs.length?'Checked references: '+s.refs.join(' ; '):''}\nFull companion source passage:\n${s.original}\n\nTeaching deck: concise wording, original section sequence. Generated plots retain source data and geometries; axis labels clarify units. Random illustrations use documented fixed seeds. See the deck source notes for corrections and provenance limits.`;
}
const raw=path.join(build,'draft.pptx');
await (await PresentationFile.exportPptx(deck)).save(raw);
// Apply Arabic language and paragraph direction metadata in the editable PPTX.
execFileSync(path.join(runtime,'python/bin/python3'),[path.join(root,'20261/scripts/teaching-slides/rtl.py'),raw,path.join(build,'candidate.pptx')],{stdio:'inherit'});
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
const finalPath=path.join(out,process.env.DECK_FILENAME||(moduleNumber===1?'module01-introduction-to-r.pptx':'module02-descriptive-statistics.pptx'));
const result=await finalizePresentation({workspaceDir:root,candidatePath:path.join(build,'candidate.pptx'),finalPath,explicitTotalSlideCount:data.length,requiredNativeTableOwnerSlides:tables,pythonExecutable:path.join(runtime,'python/bin/python3'),integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','15240000,8572500','--validate-heading-fit',...tables.flatMap(n=>['--require-native-table-slide',String(n)])],fontPolicy:{basis:'design',families:['DejaVu Sans','DejaVu Sans Mono']},verifyArtifactToolImport:true,receiptPath:path.join(build,path.basename(finalPath)+'.validation.json')});
console.log(JSON.stringify({finalPath:result.finalPath,slideCount:data.length,package:result.packageIntegrity.status,layoutFindings:result.presentationLayout.finding_count}));
