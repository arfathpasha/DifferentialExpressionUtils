/*
A KBase module: DifferentialExpressionUtils
*/

module DifferentialExpressionUtils {

/**
    A KBase module: DifferentialExpressionUtils

    This module uploads, downloads and exports DifferentialExpression and ExpressionMatrix objects
**/

   /* A boolean - 0 for false, 1 for true.
       @range (0, 1)
   */

    typedef int boolean;

   /**    Required input parameters for uploading Differential expression data

        string   destination_ref        -   object reference of Differential expression data.
                                            The object ref is 'ws_name_or_id/obj_name_or_id'
                                            where ws_name_or_id is the workspace name or id
                                            and obj_name_or_id is the object name or id

        string   diffexpr_filepath      -   file path of the differential expression data file
                                            created by cuffdiff, deseq or ballgown

        string   tool_used              -   cufflinks, ballgown or deseq
        string   tool_version           -   version of the tool used
        string   genome_ref             -   genome object reference
    **/

    typedef structure {

        string   destination_ref;
        string   diffexpr_filepath;
        string   tool_used;
        string   tool_version;
        string   genome_ref;

        string   description;               /* Optional */
        string   type;                      /* Optional - default is 'log2_level'  */
        string   scale;                     /* Optional - default is 1.0  */

    }  UploadDifferentialExpressionParams;


    /**     Output from upload differential expression    **/

    typedef structure {
        string   diffExprMatrixSet_ref;
     }  UploadDifferentialExpressionOutput;

    /**  Uploads the differential expression  **/

    funcdef  upload_differentialExpression(UploadDifferentialExpressionParams params)
                                   returns (UploadDifferentialExpressionOutput)
                                   authentication required;
    /**
        Required input parameters for downloading Differential expression
        string  source_ref   -      object reference of expression source. The
                                    object ref is 'ws_name_or_id/obj_name_or_id'
                                    where ws_name_or_id is the workspace name or id
                                    and obj_name_or_id is the object name or id
    **/


    typedef structure {
        string      source_ref;
    } DownloadDifferentialExpressionParams;

    /**  The output of the download method.  **/

    typedef structure {
        string    destination_dir;      /* directory containing all the downloaded files  */
    } DownloadDifferentialExpressionOutput;

    /** Downloads expression **/

    funcdef download_differentialExpression(DownloadDifferentialExpressionParams params)
                       returns (DownloadDifferentialExpressionOutput)
                       authentication required;

    /**
        Required input parameters for exporting expression

        string   source_ref 	-   object reference of Differential expression. The
                                    object ref is 'ws_name_or_id/obj_name_or_id'
                                    where ws_name_or_id is the workspace name or id
                                    and obj_name_or_id is the object name or id
     **/

    typedef structure {
        string source_ref;   /* workspace object reference */
    } ExportParams;

    typedef structure {
        string shock_id;     /* shock id of file to export */
     } ExportOutput;
    /** Wrapper function for use by in-narrative downloaders to download expressions from shock **/


    funcdef export_differentialExpression(ExportParams params)
                     returns (ExportOutput output)
                     authentication required;
};
