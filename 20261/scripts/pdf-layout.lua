-- HTML branding fragments are deliberately omitted in print. Arabic case
-- narration keeps its lang/dir attributes for Pandoc's bidirectional typesetting.
function Meta(meta)
  -- Older lessons use an HTML-only logo strip in this metadata field.
  meta['include-before'] = nil
  return meta
end
function Image(el)
  if el.src:match('%.svg$') then
    el.src = el.src:gsub('assets/', 'assets/pdf/svg/', 1):gsub('%.svg$', '.pdf')
  elseif el.src:match('%.gif$') then
    el.src = el.src:gsub('assets/', 'assets/pdf/svg/', 1):gsub('%.gif$', '.png')
  end
  return el
end
function Link(el)
  if el.target:match('%.qmd') then
    el.target = el.target:gsub('%.qmd', '.pdf')
  end
  return el
end

function Div(el)
  -- Babel selects direction from the Arabic language; avoid a second RTL wrapper.
  if el.attributes.lang == "ar" then el.attributes.dir = nil end
  return el
end

function Table(el)
  -- Reserve room for the heading and initial rows before a longtable begins.
  -- This prevents an isolated/repeated header at a page boundary.
  return {pandoc.RawBlock('latex', '\\Needspace{8\\baselineskip}'), el}
end

function Pandoc(doc)
  local has_sections = false
  doc:walk({Header = function(el)
    if el.level <= 2 then has_sections = true end
  end})
  if not has_sections then doc.meta.toc = false end
  return doc
end
