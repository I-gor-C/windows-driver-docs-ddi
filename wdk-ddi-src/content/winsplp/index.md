# Winsplp.h header


This header is used by print. For more information, see
- [print](../_print/index.md)

Winsplp.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [AddPrintDeviceObject function](nf-winsplp-addprintdeviceobject.md) | The AddPrintDeviceObject print provider function creates a device object for a print provider queue. |
| [AppendPrinterNotifyInfoData function](nf-winsplp-appendprinternotifyinfodata.md) | The print spooler's AppendPrinterNotifyInfoData function adds the contents of a specified PRINTER_NOTIFY_INFO_DATA structure to a specified PRINTER_NOTIFY_INFO structure. |
| [CallRouterFindFirstPrinterChangeNotification function](nf-winsplp-callrouterfindfirstprinterchangenotification.md) | . |
| [ClosePort function](nf-winsplp-closeport.md) | A language or port monitor's ClosePort function closes a printer port. |
| [ClosePrintProcessor function](nf-winsplp-closeprintprocessor.md) | A print processor's ClosePrintProcessor function completes the printing of a print job and makes the associated handle invalid. |
| [ControlPrintProcessor function](nf-winsplp-controlprintprocessor.md) | A print processor's ControlPrintProcessor function allows the spooler to control a print job. |
| [CreatePrinterIC function](nf-winsplp-createprinteric.md) | . |
| [DeletePrinterIC function](nf-winsplp-deleteprinteric.md) | . |
| [DevQueryPrint function](nf-winsplp-devqueryprint.md) | . |
| [GenerateCopyFilePaths function](nf-winsplp-generatecopyfilepaths.md) | A Point and Print DLL's GenerateCopyFilePaths function is used for modifying the source and destination paths used by print spoolers when they copy print queue-associated files to a print client. |
| [GetJobAttributes function](nf-winsplp-getjobattributes.md) | Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated. |
| [GetJobAttributesEx function](nf-winsplp-getjobattributesex.md) | Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated. |
| [GetPrintProcessorCapabilities function](nf-winsplp-getprintprocessorcapabilities.md) | A print processor's GetPrintProcessorCapabilities function returns capabilities associated with a specified input data type. |
| [ImpersonatePrinterClient function](nf-winsplp-impersonateprinterclient.md) | ImpersonatePrinterClient resumes impersonation of the client, completing the operation begun by RevertToPrinterSelf. |
| [InitializePrintMonitor function](nf-winsplp-initializeprintmonitor.md) | The InitializePrintMonitor function is obsolete and is supported only for compatibility purposes. |
| [InitializePrintMonitor2 function](nf-winsplp-initializeprintmonitor2.md) | A print monitor's InitializePrintMonitor2 function initializes a print monitor for use with clustered print servers. |
| [InitializePrintMonitorUI function](nf-winsplp-initializeprintmonitorui.md) | A port monitor UI DLL's InitializePrintMonitorUI function supplies the print spooler with addresses of DLL functions. |
| [InitializePrintProvidor function](nf-winsplp-initializeprintprovidor.md) | Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated. |
| [LogJobInfoForBranchOffice function](nf-winsplp-logjobinfoforbranchoffice.md) | Allows Branch Office clients to send job events to the host print server. |
| [OpenPrintProcessor function](nf-winsplp-openprintprocessor.md) | A print processor's OpenPrintProcessor function prepares the print processor for printing a job and returns a handle. |
| [PartialReplyPrinterChangeNotification function](nf-winsplp-partialreplyprinterchangenotification.md) | The print spooler's PartialReplyPrinterChangeNotification function allows a print provider to update the spooler's database of printer changes associated with a notification handle. |
| [PlayGdiScriptOnPrinterIC function](nf-winsplp-playgdiscriptonprinteric.md) | . |
| [PrintDocumentOnPrintProcessor function](nf-winsplp-printdocumentonprintprocessor.md) | A print processor's PrintDocumentOnPrintProcessor function converts a print job from a spooled format into raw data that can be sent to a print monitor. |
| [ProvidorFindClosePrinterChangeNotification function](nf-winsplp-providorfindcloseprinterchangenotification.md) | . |
| [ProvidorFindFirstPrinterChangeNotification function](nf-winsplp-providorfindfirstprinterchangenotification.md) | . |
| [ReadPort function](nf-winsplp-readport.md) | A port monitor's ReadPort function reads data from a printer port. |
| [RemovePrintDeviceObject function](nf-winsplp-removeprintdeviceobject.md) | The RemovePrintDeviceObject function removes a device object from a print provider queue. |
| [ReplyPrinterChangeNotification function](nf-winsplp-replyprinterchangenotification.md) | The print spooler's ReplyPrinterChangeNotification function allows a print provider to update the spooler's database of print queue events associated with a notification handle, and to notify the client that print queue events have occurred. |
| [ReplyPrinterChangeNotificationEx function](nf-winsplp-replyprinterchangenotificationex.md) | . |
| [RevertToPrinterSelf function](nf-winsplp-reverttoprinterself.md) | When RevertToPrinterSelf is called on an impersonating thread, it returns the token for the thread that is being impersonated. |
| [RouterAllocBidiMem function](nf-winsplp-routerallocbidimem.md) | RouterAllocBidiMem allocates a block of memory of a specified size. This function is used by the port monitor to allocate memory for strings and binary objects. |
| [RouterAllocBidiResponseContainer function](nf-winsplp-routerallocbidiresponsecontainer.md) | RouterAllocBidiResponseContainer allocates a BIDI_RESPONSE_CONTAINER structure containing a list of bidi responses. The bidi response list is an array of BIDI_RESPONSE_DATA structures. |
| [RouterAllocPrinterNotifyInfo function](nf-winsplp-routerallocprinternotifyinfo.md) | The print spooler's RouterAllocPrinterNotifyInfo function allocates a PRINTER_NOTIFY_INFO structure and an array of PRINTER_NOTIFY_INFO_DATA structures. |
| [RouterFreeBidiMem function](nf-winsplp-routerfreebidimem.md) | RouterFreeBidiMem frees a block of memory that was previously allocated by RouterAllocBidiMem. |
| [RouterFreeBidiResponseContainer function](nf-winsplp-routerfreebidiresponsecontainer.md) | RouterFreeBidiResponseContainer frees a BIDI_RESPONSE_CONTAINER structure previously allocated by RouterAllocBidiResponseContainer. |
| [RouterFreePrinterNotifyInfo function](nf-winsplp-routerfreeprinternotifyinfo.md) | The print spooler's RouterFreePrinterNotifyInfo function deallocates a specified PRINTER_NOTIFY_INFO structure and its associated PRINTER_NOTIFY_INFO_DATA structure array. |
| [SplDeleteSpoolerPortEnd function](nf-winsplp-spldeletespoolerportend.md) | . |
| [SplDeleteSpoolerPortStart function](nf-winsplp-spldeletespoolerportstart.md) | . |
| [SplIsSessionZero function](nf-winsplp-splissessionzero.md) | The SplIsSessionZero function determines whether a certain print job (print handle plus job ID) was issued in session zero. |
| [SplPromptUIInUsersSession function](nf-winsplp-splpromptuiinuserssession.md) | The SplPromptUIInUsersSession function displays a standard message box in the session indicated by the printer handle and job ID. |
| [SpoolerCopyFileEvent function](nf-winsplp-spoolercopyfileevent.md) | A Point and Print DLL's SpoolerCopyFileEvent function receives notifications of events associated with copying print queue-associated files to a print client, when the client connects to a print server. |
| [SpoolerFindClosePrinterChangeNotification function](nf-winsplp-spoolerfindcloseprinterchangenotification.md) | . |
| [SpoolerFindFirstPrinterChangeNotification function](nf-winsplp-spoolerfindfirstprinterchangenotification.md) | . |
| [SpoolerFindNextPrinterChangeNotification function](nf-winsplp-spoolerfindnextprinterchangenotification.md) | . |
| [SpoolerFreePrinterNotifyInfo function](nf-winsplp-spoolerfreeprinternotifyinfo.md) | . |
| [SpoolerRefreshPrinterChangeNotification function](nf-winsplp-spoolerrefreshprinterchangenotification.md) | . |
| [UpdatePrintDeviceObject function](nf-winsplp-updateprintdeviceobject.md) | The UpdatePrintDeviceObject function updates the properties of a device object that is in the print provider queue. |
| [WritePort function](nf-winsplp-writeport.md) | A port monitor's WritePort function writes data to a printer port. |
| [XcvClosePort function](nf-winsplp-xcvcloseport.md) | A port monitor server DLL's XcvClosePort function closes a printer port that was opened by XcvOpenPort. |
| [XcvDataPort function](nf-winsplp-xcvdataport.md) | A port monitor server DLL's XcvDataPort function receives information from, and returns information to, the port monitor's UI DLL. |
| [XcvOpenPort function](nf-winsplp-xcvopenport.md) | A port monitor server DLL's XcvOpenPort function opens a port for configuration operations. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [ROUTER_NOTIFY_CALLBACK callback](nc-winsplp-router-notify-callback.md) | . |

## Structures

| Title   | Description   |
| ---- |:---- |
| [LPBranchOfficeJobDataContainer structure](ns-winsplp-lpbranchofficejobdatacontainer.md) | This structure defines a container for one or more BranchOfficeJobData structures to sent to a server. |
| [MONITOR structure](ns-winsplp--monitor.md) | The MONITOR structure is obsolete and is supported only for compatibility reasons. |
| [MONITOR2 structure](ns-winsplp--monitor2.md) | The MONITOR2 structure contains pointers to the functions defined by print monitors. |
| [MONITOREX structure](ns-winsplp--monitorex.md) | The MONITOREX structure is obsolete and supported for compatibility purposes only. |
| [MONITORINIT structure](ns-winsplp--monitorinit.md) | The MONITORINIT structure is used as an input parameter to a print monitor's InitializePrintMonitor2 function. |
| [MONITORREG structure](ns-winsplp--monitorreg.md) | The MONITORREG structure supplies print monitors with the address of registry functions to use instead of Win32 registry API functions. |
| [MONITORUI structure](ns-winsplp--monitorui.md) | The MONITORUI structure contains pointers to the functions within a port monitor UI DLL that the print spooler calls. |
| [NOTIFICATION_CONFIG_1 structure](ns-winsplp--notification-config-1.md) | . |
| [PBranchOfficeJobData structure](ns-winsplp-pbranchofficejobdata.md) | This structure contains the type of event to log (eEventType), the job ID, and the data required by the event. |
| [PBranchOfficeJobDataError structure](ns-winsplp-pbranchofficejobdataerror.md) | This structure contains the necessary data for logging a branch office job failure event on a remote server. This is based on standard job-related data available to the spooler. |
| [PBranchOfficeJobDataPipelineFailed structure](ns-winsplp-pbranchofficejobdatapipelinefailed.md) | Contains the necessary data for logging a branch office job Pipeline Rendering Failed event on a remote server. This is based on standard job-related data available to the spooler. |
| [PBranchOfficeJobDataPrinted structure](ns-winsplp-pbranchofficejobdataprinted.md) | Contains the necessary data for logging a branch office job completed event on a remote server. This is based on standard job-related data available to the spooler. |
| [PBranchOfficeJobDataRendered structure](ns-winsplp-pbranchofficejobdatarendered.md) | Contains the necessary data for logging a branch office job Pipeline Rendering Event on a remote server. This is based on job-related data available to the spooler. |
| [PBranchOfficeLogOfflineFileFull structure](ns-winsplp-pbranchofficelogofflinefilefull.md) | Contains the necessary data for logging that the offline log archive on the current client overflowed at some point. |
| [PMESSAGEBOX_PARAMS structure](ns-winsplp-pmessagebox-params.md) | The MESSAGEBOX_PARAMS structure is used by the SplPromptUIInUsersSession function to hold information about the appearance and behavior of a message box. |
| [PRINTER_NOTIFY_INIT structure](ns-winsplp--printer-notify-init.md) | . |
| [PRINTPROCESSOROPENDATA structure](ns-winsplp--printprocessoropendata.md) | The PRINTPROCESSOROPENDATA structure is used as an input parameter to a print processor's OpenPrintProcessor function. |
| [PRINTPROVIDOR structure](ns-winsplp--printprovidor.md) | Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated. |
| [PSHOWUIPARAMS structure](ns-winsplp-pshowuiparams.md) | The SplPromptUIInUsersSession function uses the SHOWUIPARAMS structure to hold information about the appearance and behavior of a message box. |
| [SPLCLIENT_INFO_1 structure](ns-winsplp--splclient-info-1.md) | The SPLCLIENT_INFO_1 structure is used as input to the GenerateCopyFilePaths function that is exported by Point and Print DLLs. |
| [SPLCLIENT_INFO_2_V1 structure](ns-winsplp--splclient-info-2-v1.md) | Contains the handle for the server-side printer that is used to make direct API calls from the client to the server without the overhead of the RPC. |
| [SPLCLIENT_INFO_2_V2 structure](ns-winsplp--splclient-info-2-v2.md) | . |
| [SPLCLIENT_INFO_2_V3 structure](ns-winsplp--splclient-info-2-v3.md) | . |
| [SPLCLIENT_INFO_3_VISTA structure](ns-winsplp--splclient-info-3-vista.md) | Contains a super-set of the information in both a SPLCLIENT_INFO_1 and SPLCLIENT_INFO_2 structure. It also contains additional information needed by the provider. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [NOTIFICATION_CALLBACK_COMMANDS enumeration](ne-winsplp--notification-callback-commands.md) | . |
| [NOTIFICATION_CONFIG_FLAGS enumeration](ne-winsplp--notification-config-flags.md) | . |
| [UI_TYPE enumeration](ne-winsplp-ui-type.md) | . |
