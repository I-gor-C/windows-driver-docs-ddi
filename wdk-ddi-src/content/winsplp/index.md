---
UID : NA:winsplp
ms.assetid : e65d4581-0840-38bd-9afe-5a9d19c9769b
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# winsplp.h header



winsplp.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [ROUTER_NOTIFY_CALLBACK](nc-winsplp-router_notify_callback.md) | "." |
| [AddPortUI](nf-winsplp-addportui.md) | A port monitor UI DLL's AddPortUI function adds a printer port, then obtains port configuration information from the user and sends it to the port monitor server DLL. |
| [AddPrintDeviceObject](nf-winsplp-addprintdeviceobject.md) | The AddPrintDeviceObject print provider function creates a device object for a print provider queue. |
| [AppendPrinterNotifyInfoData](nf-winsplp-appendprinternotifyinfodata.md) | The print spooler's AppendPrinterNotifyInfoData function adds the contents of a specified PRINTER_NOTIFY_INFO_DATA structure to a specified PRINTER_NOTIFY_INFO structure. |
| [CallRouterFindFirstPrinterChangeNotification](nf-winsplp-callrouterfindfirstprinterchangenotification.md) | "." |
| [ClosePort](nf-winsplp-closeport.md) | A language or port monitor's ClosePort function closes a printer port. |
| [ClosePrintProcessor](nf-winsplp-closeprintprocessor.md) | A print processor's ClosePrintProcessor function completes the printing of a print job and makes the associated handle invalid. |
| [ConfigurePortUI](nf-winsplp-configureportui.md) | A port monitor UI DLL's ConfigurePortUI function obtains port configuration information from the user and sends it to the port monitor server DLL. |
| [ControlPrintProcessor](nf-winsplp-controlprintprocessor.md) | A print processor's ControlPrintProcessor function allows the spooler to control a print job. |
| [CreatePrinterIC](nf-winsplp-createprinteric.md) | "." |
| [DeletePortUI](nf-winsplp-deleteportui.md) | A port monitor UI DLL's DeletePortUI function deletes a printer port. |
| [DeletePrinterIC](nf-winsplp-deleteprinteric.md) | "." |
| [DevQueryPrint](nf-winsplp-devqueryprint.md) | "." |
| [GenerateCopyFilePaths](nf-winsplp-generatecopyfilepaths.md) | A Point and Print DLL's GenerateCopyFilePaths function is used for modifying the source and destination paths used by print spoolers when they copy print queue-associated files to a print client. |
| [GetJobAttributes](nf-winsplp-getjobattributes.md) | Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated. |
| [GetJobAttributesEx](nf-winsplp-getjobattributesex.md) | Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated. |
| [GetPrintProcessorCapabilities](nf-winsplp-getprintprocessorcapabilities.md) | A print processor's GetPrintProcessorCapabilities function returns capabilities associated with a specified input data type. |
| [ImpersonatePrinterClient](nf-winsplp-impersonateprinterclient.md) | ImpersonatePrinterClient resumes impersonation of the client, completing the operation begun by RevertToPrinterSelf. |
| [InitializeMonitor](nf-winsplp-initializemonitor.md) | "." |
| [InitializeMonitorEx](nf-winsplp-initializemonitorex.md) | "." |
| [InitializePrintMonitor](nf-winsplp-initializeprintmonitor.md) | The InitializePrintMonitor function is obsolete and is supported only for compatibility purposes. |
| [InitializePrintMonitor2](nf-winsplp-initializeprintmonitor2.md) | A print monitor's InitializePrintMonitor2 function initializes a print monitor for use with clustered print servers. |
| [InitializePrintMonitorUI](nf-winsplp-initializeprintmonitorui.md) | A port monitor UI DLL's InitializePrintMonitorUI function supplies the print spooler with addresses of DLL functions. |
| [InitializePrintProvidor](nf-winsplp-initializeprintprovidor.md) | Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated. |
| [LogJobInfoForBranchOffice](nf-winsplp-logjobinfoforbranchoffice.md) | Allows Branch Office clients to send job events to the host print server. |
| [OpenPort](nf-winsplp-openport.md) | A port monitor's OpenPort function opens a printer port. |
| [OpenPrintProcessor](nf-winsplp-openprintprocessor.md) | A print processor's OpenPrintProcessor function prepares the print processor for printing a job and returns a handle. |
| [PartialReplyPrinterChangeNotification](nf-winsplp-partialreplyprinterchangenotification.md) | The print spooler's PartialReplyPrinterChangeNotification function allows a print provider to update the spooler's database of printer changes associated with a notification handle. |
| [PlayGdiScriptOnPrinterIC](nf-winsplp-playgdiscriptonprinteric.md) | "." |
| [PrintDocumentOnPrintProcessor](nf-winsplp-printdocumentonprintprocessor.md) | A print processor's PrintDocumentOnPrintProcessor function converts a print job from a spooled format into raw data that can be sent to a print monitor. |
| [ProvidorFindClosePrinterChangeNotification](nf-winsplp-providorfindcloseprinterchangenotification.md) | "." |
| [ProvidorFindFirstPrinterChangeNotification](nf-winsplp-providorfindfirstprinterchangenotification.md) | "." |
| [ReadPort](nf-winsplp-readport.md) | A port monitor's ReadPort function reads data from a printer port. |
| [RemovePrintDeviceObject](nf-winsplp-removeprintdeviceobject.md) | The RemovePrintDeviceObject function removes a device object from a print provider queue. |
| [ReplyPrinterChangeNotification](nf-winsplp-replyprinterchangenotification.md) | The print spooler's ReplyPrinterChangeNotification function allows a print provider to update the spooler's database of print queue events associated with a notification handle, and to notify the client that print queue events have occurred. |
| [ReplyPrinterChangeNotificationEx](nf-winsplp-replyprinterchangenotificationex.md) | "." |
| [RevertToPrinterSelf](nf-winsplp-reverttoprinterself.md) | When RevertToPrinterSelf is called on an impersonating thread, it returns the token for the thread that is being impersonated. |
| [RouterAllocBidiMem](nf-winsplp-routerallocbidimem.md) | RouterAllocBidiMem allocates a block of memory of a specified size. This function is used by the port monitor to allocate memory for strings and binary objects. |
| [RouterAllocBidiResponseContainer](nf-winsplp-routerallocbidiresponsecontainer.md) | RouterAllocBidiResponseContainer allocates a BIDI_RESPONSE_CONTAINER structure containing a list of bidi responses. The bidi response list is an array of BIDI_RESPONSE_DATA structures. |
| [RouterAllocPrinterNotifyInfo](nf-winsplp-routerallocprinternotifyinfo.md) | The print spooler's RouterAllocPrinterNotifyInfo function allocates a PRINTER_NOTIFY_INFO structure and an array of PRINTER_NOTIFY_INFO_DATA structures. |
| [RouterFreeBidiMem](nf-winsplp-routerfreebidimem.md) | RouterFreeBidiMem frees a block of memory that was previously allocated by RouterAllocBidiMem. |
| [RouterFreeBidiResponseContainer](nf-winsplp-routerfreebidiresponsecontainer.md) | RouterFreeBidiResponseContainer frees a BIDI_RESPONSE_CONTAINER structure previously allocated by RouterAllocBidiResponseContainer. |
| [RouterFreePrinterNotifyInfo](nf-winsplp-routerfreeprinternotifyinfo.md) | The print spooler's RouterFreePrinterNotifyInfo function deallocates a specified PRINTER_NOTIFY_INFO structure and its associated PRINTER_NOTIFY_INFO_DATA structure array. |
| [SplDeleteSpoolerPortEnd](nf-winsplp-spldeletespoolerportend.md) | "." |
| [SplDeleteSpoolerPortStart](nf-winsplp-spldeletespoolerportstart.md) | "." |
| [SplIsSessionZero](nf-winsplp-splissessionzero.md) | The SplIsSessionZero function determines whether a certain print job (print handle plus job ID) was issued in session zero. |
| [SplPromptUIInUsersSession](nf-winsplp-splpromptuiinuserssession.md) | The SplPromptUIInUsersSession function displays a standard message box in the session indicated by the printer handle and job ID. |
| [SpoolerCopyFileEvent](nf-winsplp-spoolercopyfileevent.md) | A Point and Print DLL's SpoolerCopyFileEvent function receives notifications of events associated with copying print queue-associated files to a print client, when the client connects to a print server. |
| [SpoolerFindClosePrinterChangeNotification](nf-winsplp-spoolerfindcloseprinterchangenotification.md) | "." |
| [SpoolerFindFirstPrinterChangeNotification](nf-winsplp-spoolerfindfirstprinterchangenotification.md) | "." |
| [SpoolerFindNextPrinterChangeNotification](nf-winsplp-spoolerfindnextprinterchangenotification.md) | "." |
| [SpoolerFreePrinterNotifyInfo](nf-winsplp-spoolerfreeprinternotifyinfo.md) | "." |
| [SpoolerRefreshPrinterChangeNotification](nf-winsplp-spoolerrefreshprinterchangenotification.md) | "." |
| [UpdatePrintDeviceObject](nf-winsplp-updateprintdeviceobject.md) | The UpdatePrintDeviceObject function updates the properties of a device object that is in the print provider queue. |
| [WritePort](nf-winsplp-writeport.md) | A port monitor's WritePort function writes data to a printer port. |
| [XcvClosePort](nf-winsplp-xcvcloseport.md) | A port monitor server DLL's XcvClosePort function closes a printer port that was opened by XcvOpenPort. |
| [XcvDataPort](nf-winsplp-xcvdataport.md) | A port monitor server DLL's XcvDataPort function receives information from, and returns information to, the port monitor's UI DLL. |
| [XcvOpenPort](nf-winsplp-xcvopenport.md) | A port monitor server DLL's XcvOpenPort function opens a port for configuration operations. |



## Structures
| Title | Description |
| ---- |:---- |
| [_MONITOR](ns-winsplp-_monitor.md) | The MONITOR structure is obsolete and is supported only for compatibility reasons. |
| [_MONITOR2](ns-winsplp-_monitor2.md) | The MONITOR2 structure contains pointers to the functions defined by print monitors. |
| [_MONITOREX](ns-winsplp-_monitorex.md) | The MONITOREX structure is obsolete and supported for compatibility purposes only. |
| [_MONITORINIT](ns-winsplp-_monitorinit.md) | The MONITORINIT structure is used as an input parameter to a print monitor's InitializePrintMonitor2 function. |
| [_MONITORREG](ns-winsplp-_monitorreg.md) | The MONITORREG structure supplies print monitors with the address of registry functions to use instead of Win32 registry API functions. |
| [_MONITORUI](ns-winsplp-_monitorui.md) | The MONITORUI structure contains pointers to the functions within a port monitor UI DLL that the print spooler calls. |
| [_NOTIFICATION_CONFIG_1](ns-winsplp-_notification_config_1.md) | "." |
| [_PRINTER_NOTIFY_INIT](ns-winsplp-_printer_notify_init.md) | "." |
| [_PRINTPROCESSOROPENDATA](ns-winsplp-_printprocessoropendata.md) | The PRINTPROCESSOROPENDATA structure is used as an input parameter to a print processor's OpenPrintProcessor function. |
| [_PRINTPROVIDOR](ns-winsplp-_printprovidor.md) | Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated. |
| [_SPLCLIENT_INFO_1](ns-winsplp-_splclient_info_1.md) | The SPLCLIENT_INFO_1 structure is used as input to the GenerateCopyFilePaths function that is exported by Point and Print DLLs. |
| [_SPLCLIENT_INFO_2_V1](ns-winsplp-_splclient_info_2_v1.md) | Contains the handle for the server-side printer that is used to make direct API calls from the client to the server without the overhead of the RPC. |
| [_SPLCLIENT_INFO_2_V2](ns-winsplp-_splclient_info_2_v2.md) | "." |
| [_SPLCLIENT_INFO_2_V3](ns-winsplp-_splclient_info_2_v3.md) | "." |
| [_SPLCLIENT_INFO_3_VISTA](ns-winsplp-_splclient_info_3_vista.md) | Contains a super-set of the information in both a SPLCLIENT_INFO_1 and SPLCLIENT_INFO_2 structure. It also contains additional information needed by the provider. |
| [BranchOfficeJobData](ns-winsplp-branchofficejobdata.md) | This structure contains the type of event to log (eEventType), the job ID, and the data required by the event. |
| [BranchOfficeJobDataContainer](ns-winsplp-branchofficejobdatacontainer.md) | This structure defines a container for one or more BranchOfficeJobData structures to sent to a server. |
| [BranchOfficeJobDataError](ns-winsplp-branchofficejobdataerror.md) | This structure contains the necessary data for logging a branch office job failure event on a remote server. This is based on standard job-related data available to the spooler. |
| [BranchOfficeJobDataPipelineFailed](ns-winsplp-branchofficejobdatapipelinefailed.md) | Contains the necessary data for logging a branch office job Pipeline Rendering Failed event on a remote server. This is based on standard job-related data available to the spooler. |
| [BranchOfficeJobDataPrinted](ns-winsplp-branchofficejobdataprinted.md) | Contains the necessary data for logging a branch office job completed event on a remote server. This is based on standard job-related data available to the spooler. |
| [BranchOfficeJobDataRendered](ns-winsplp-branchofficejobdatarendered.md) | Contains the necessary data for logging a branch office job Pipeline Rendering Event on a remote server. This is based on job-related data available to the spooler. |
| [BranchOfficeLogOfflineFileFull](ns-winsplp-branchofficelogofflinefilefull.md) | Contains the necessary data for logging that the offline log archive on the current client overflowed at some point. |
| [MESSAGEBOX_PARAMS](ns-winsplp-messagebox_params.md) | The MESSAGEBOX_PARAMS structure is used by the SplPromptUIInUsersSession function to hold information about the appearance and behavior of a message box. |
| [SHOWUIPARAMS](ns-winsplp-showuiparams.md) | The SplPromptUIInUsersSession function uses the SHOWUIPARAMS structure to hold information about the appearance and behavior of a message box. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_NOTIFICATION_CALLBACK_COMMANDS](ne-winsplp-_notification_callback_commands.md) | "." |
| [_NOTIFICATION_CONFIG_FLAGS](ne-winsplp-_notification_config_flags.md) | "." |
| [UI_TYPE](ne-winsplp-ui_type.md) | "." |