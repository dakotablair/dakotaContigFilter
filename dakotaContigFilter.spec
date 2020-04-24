/*
A KBase module: dakotaContigFilter
This sample module contains one small method that filters contigs.
*/

module dakotaContigFilter {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_dakotaContigFilter(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
