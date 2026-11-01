import fs from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
// The package is resolved from the bundled runtime, without a project dependency.
const runtime = '/home/me/.cache/codex-runtimes/codex-primary-runtime/dependencies';
process.env.RUNTIME_NODE_MODULES = path.join(runtime, 'node/node_modules');
const { Presentation, PresentationFile } = await import(pathToFileURL(path.join(runtime, 'node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs')).href);
const root = process.cwd();
const skill = '/home/me/.codex/plugins/cache/openai-primary-runtime/presentations/26.1022.11436/skills/presentations';
const build = path.join(root, '20261/_output/.chapter01-build');
const out = path.join(root, '20261/_output/book-chapters/basic-business-statistics-13e');
await fs.mkdir(build, {recursive:true});
await fs.mkdir(out, {recursive:true});
const cards = JSON.parse(await fs.readFile(path.join(root, '20261/book-chapters/basic-business-statistics-13e/chapter01-cards.json'), 'utf8'));
const deck = Presentation.create({slideSize:{width:1280,height:720}});
const C = {plum:'#493347',ink:'#2F343B',muted:'#56616D',pale:'#F5EDF4',blue:'#356B8C'};
function text(slide, value, top, height, size=42, color=C.ink, font='DejaVu Sans', bold=false) {
  const box = slide.shapes.add({geometry:'textbox',position:{left:80,top,width:1120,height},fill:'none',line:{fill:'none',width:0}});
  box.text = value;
  box.text.style = {typeface:font,fontSize:size,color,bold,verticalAlignment:'top',insets:0,wrap:'none',autoFit:'none'};
  return box;
}
const intro=deck.slides.add(); intro.background.fill=C.pale;
text(intro,'Basic Business Statistics / 13th edition',78,55,28,C.plum);
text(intro,'Defining and Collecting Data',172,100,52,C.plum,'DejaVu Sans',true);
text(intro,'50 flashcards for quick recall',304,60,38);
text(intro,'Read the question. Recall the answer.\nAdvance one page to check.',430,120,32);
text(intro,'Chapter 1 / Based on the supplied teaching guide',634,35,22,C.muted);
intro.speakerNotes.text='50 question-and-answer cards based on the user-supplied Chapter 1 summary and teaching guide. Textbook pages, datasets, and edition claims were not independently verified. Source text is preserved separately.';
for (let i=0;i<cards.length;i++) {
  const c=cards[i];
  for (const side of ['question','answer']) {
    const s=deck.slides.add(); s.background.fill=side==='question'?C.pale:'#FFFFFF';
    text(s,`CHAPTER 1     ${String(i+1).padStart(2,'0')} / 50     ${side.toUpperCase()}`,46,35,22,C.muted);
    text(s,c.topic,107,60,40,C.plum,'DejaVu Sans',true);
    const code=side==='question'?c.promptCode:c.code;
    text(s,side==='question'?c.question:c.answer,210,code?125:350,36);
    if(code) text(s,code,360,220,25,C.blue,'DejaVu Sans Mono');
    text(s,side==='question'?'Recall your answer, then advance.':c.cue,638,40,22,C.muted);
    s.speakerNotes.text=`Source: supplied Chapter 1 guide, Basic Business Statistics: Concepts and Applications, 13th edition. ${c.source}. ${c.notes||''} A shortened review card. See the full lesson for explanations and prerequisites.`;
  }
}
for (let i=0;i<deck.slides.items.length;i++) {
  const png=await deck.export({slide:deck.slides.items[i],format:'png',scale:1});
  await fs.writeFile(path.join(build,`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await png.arrayBuffer()));
}
const candidate=path.join(build,'candidate.pptx');
await (await PresentationFile.exportPptx(deck)).save(candidate);
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
const result=await finalizePresentation({workspaceDir:root,candidatePath:candidate,finalPath:path.join(out,'chapter01-flashcards.pptx'),pythonExecutable:path.join(runtime,'python/bin/python3'),integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit'],fontPolicy:{basis:'design',families:['DejaVu Sans','DejaVu Sans Mono']},verifyArtifactToolImport:true,receiptPath:path.join(build,'validation.json')});
console.log(JSON.stringify(result));
