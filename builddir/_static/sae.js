DESELEMENT = "h2,h3,h4"; //"h1,h2,h3,h4,ul,div.section p,div.highlight-python";

function strip_tags(st) {
    return st.replace(/<[^>]+>?[^<]*>/g, '');
}
