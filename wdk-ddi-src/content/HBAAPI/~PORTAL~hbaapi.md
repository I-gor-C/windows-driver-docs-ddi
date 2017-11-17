# Declarations in the hbaapi header
This header Hbaapi contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SMHBA_PhyStatistics structure](ns-hbaapi-smhba-phystatistics.md) | TBD |
| [HBA_EventInfo structure](ns-hbaapi-hba-eventinfo.md) | The HBA_EventInfo structure contains information about an event of the indicated type. |
| [HBA_FCPBinding structure](ns-hbaapi-hba-fcpbinding.md) | The HBA_FCPBinding structure contains an array of bindings between operating system and fibre channel protocol (FCP) identifiers for a set of logical units. |
| [HBA_FCPBindingEntry2 structure](ns-hbaapi-hba-fcpbindingentry2.md) | The HBA_FCPBindingEntry2 structure defines a binding between the information that uniquely identifies a logical unit for the operating system and the fibre channel protocol (FCP) identifier for the logical unit. |
| [HBA_PortStatistics structure](ns-hbaapi-hba-portstatistics.md) | The HBA_PortStatistics structure contains statistical information about a port. |
| [SMHBA_TargetMapping structure](ns-hbaapi-smhba-targetmapping.md) | TBD |
| [HBA_RSCN_EventInfo structure](ns-hbaapi-hba-rscn-eventinfo.md) | The HBA_Link_EventInfo structure contains information about a WMI RSCN event associated with the fibre channel HBA API. |
| [HBA_ScsiId structure](ns-hbaapi-hba-scsiid.md) | The HBA_ScsiId structure contains information used by the operating system to identify a SCSI logical unit. |
| [SMHBA_SAS_Port structure](ns-hbaapi-smhba-sas-port.md) | TBD |
| [SMHBA_Port structure](ns-hbaapi-smhba-port.md) | TBD |
| [HBA_SBDskCapacity structure](ns-hbaapi-hba-sbdskcapacity.md) | TBD |
| [HBA_SBDevId structure](ns-hbaapi-hba-sbdevid.md) | TBD |
| [HBA_PortAttributes structure](ns-hbaapi-hba-portattributes.md) | The structure is used by the HBA_GetPortAttributesByWWN fibre channel HBA library routine to report the attributes for a specified remote fibre channel port. |
| [HBA_LUID structure](ns-hbaapi-hba-luid.md) | The HBA_LUID structure contains the identification descriptor from the device identification page of the vital products data returned by a SCSI INQUIRY command. |
| [SMHBA_ScsiId structure](ns-hbaapi-smhba-scsiid.md) | TBD |
| [SMHBA_Binding structure](ns-hbaapi-smhba-binding.md) | TBD |
| [HBA_wwn structure](ns-hbaapi-hba-wwn.md) | The HBA_wwn structure contains a 64 bit world-wide name (WWN) that uniquely identifies an HBA. |
| [SMHBA_LUID structure](ns-hbaapi-smhba-luid.md) | TBD |
| [SMHBA_PortAttributes structure](ns-hbaapi-smhba-portattributes.md) | TBD |
| [HBA_Ned structure](ns-hbaapi-hba-ned.md) | TBD |
| [SMHBA_FC_Phy structure](ns-hbaapi-smhba-fc-phy.md) | TBD |
| [SMHBA_SCSILUN structure](ns-hbaapi-smhba-scsilun.md) | TBD |
| [HBA_FCPBinding2 structure](ns-hbaapi-hba-fcpbinding2.md) | The HBA_FCPBinding2 structure contains an array of bindings between operating system identifiers, SCSI logical unit ID descriptors (LUIDs) and fibre channel protocol (FCP) identifiers for a set of logical units. |
| [HBA_FcpScsiEntry structure](ns-hbaapi-hba-fcpscsientry.md) | The HBA_FcpScsiEntry structure defines a mapping between an operating system identifier for a logical unit and the corresponding fibre channel protocol (FCP) identifier for the logical unit. |
| [HBA_Link_EventInfo structure](ns-hbaapi-hba-link-eventinfo.md) | The HBA_Link_EventInfo structure contains information about a WMI link event associated with the fibre channel HBA API. |
| [SMHBA_SASPhyStatistics structure](ns-hbaapi-smhba-sasphystatistics.md) | TBD |
| [HBA_ipaddress structure](ns-hbaapi-hba-ipaddress.md) | The HBA_ipaddress structure specifies an IP address in a way that is independent of the version of the IP protocol in use. |
| [HBA_FCPTargetMapping structure](ns-hbaapi-hba-fcptargetmapping.md) | The HBA_FCPTargetMapping structure contains an array of bindings between operating system and fibre channel protocol (FCP) identifiers for a set of target devices. |
| [HBA_FC4Statistics structure](ns-hbaapi-hba-fc4statistics.md) | The HBA_FC4Statistics structure contains port statistics. |
| [HBA_FCPBindingEntry structure](ns-hbaapi-hba-fcpbindingentry.md) | TBD |
| [HBA_DeviceSelfDesc structure](ns-hbaapi-hba-deviceselfdesc.md) | TBD |
| [SMHBA_SAS_Phy structure](ns-hbaapi-smhba-sas-phy.md) | TBD |
| [SMHBA_ScsiEntry structure](ns-hbaapi-smhba-scsientry.md) | TBD |
| [HBA_FCPTargetMappingV2 structure](ns-hbaapi-hba-fcptargetmappingv2.md) | The HBA_FCPTargetMappingV2 structure contains a variable length array of target mappings. |
| [HBA_LibraryAttributes structure](ns-hbaapi-hba-libraryattributes.md) | The HBA_LibraryAttributes structure holds the library attributes. |
| [HBA_FcpScsiEntryV2 structure](ns-hbaapi-hba-fcpscsientryv2.md) | The HBA_FcpScsiEntryV2 structure defines a mapping between an operating system identifier for a logical unit and the corresponding fibre channel protocol (FCP) identifier for the logical unit. |
| [SMHBA_FC_Port structure](ns-hbaapi-smhba-fc-port.md) | TBD |
| [HBA_MgmtInfo structure](ns-hbaapi-hba-mgmtinfo.md) | The HBA_MgmtInfo structure is used in conjunction with the HBA_SetRNIDMgmtInfo routine to program the HBA to return the indicated request node identification information data (RNID). |
| [HBA_Pty_EventInfo structure](ns-hbaapi-hba-pty-eventinfo.md) | The HBA_Link_EventInfo structure contains information about a WMI proprietary event associated with the fibre channel HBA API. |
| [SMHBA_BindingEntry structure](ns-hbaapi-smhba-bindingentry.md) | TBD |
| [HBA_FcpId structure](ns-hbaapi-hba-fcpid.md) | The HBA_FcpId structure is identical to the HBAFCPID structure. |
| [SMHBA_LibraryAttributes structure](ns-hbaapi-smhba-libraryattributes.md) | TBD |
| [SMHBA_PORTLUN structure](ns-hbaapi-smhba-portlun.md) | TBD |
| [SMHBA_ProtocolStatistics structure](ns-hbaapi-smhba-protocolstatistics.md) | TBD |
| [SMHBA_AdapterAttributes structure](ns-hbaapi-smhba-adapterattributes.md) | TBD |
| [HBA_AdapterAttributes structure](ns-hbaapi-hba-adapterattributes.md) | The HBA_AdapterAttributes structure is used in conjunction with the HBA_GetAdapterAttributes routine to report the attributes of an HBA. |
| [HBA_fc4types structure](ns-hbaapi-hba-fc4types.md) | The HBA_fc4types structure contains a set of up to 32 values indicating the FC-4 types that the HBA supports. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [HBA_GetSBStatistics function](nf-hbaapi-hba-getsbstatistics.md) | TBD |
| [HBA_GetVersion function](nf-hbaapi-hba-getversion.md) | The HBA_GetVersion routine returns the version of the fibre channel HBA API specification with which the HBA API library is compatible. |
| [HBA_SendReadCapacity function](nf-hbaapi-hba-sendreadcapacity.md) | The HBA_SendReadCapacity routine sends a SCSI read capacity command to the indicated remote port. |
| [SMHBA_RegisterForAdapterPortEvents function](nf-hbaapi-smhba-registerforadapterportevents.md) | TBD |
| [SMHBA_GetTargetMapping function](nf-hbaapi-smhba-gettargetmapping.md) | TBD |
| [HBA_RefreshInformation function](nf-hbaapi-hba-refreshinformation.md) | The HBA_RefreshInformation routine refreshes the library's internally cached data for the indicated HBA. |
| [SMHBA_ScsiReportLuns function](nf-hbaapi-smhba-scsireportluns.md) | TBD |
| [HBA_GetRNIDMgmtInfo function](nf-hbaapi-hba-getrnidmgmtinfo.md) | The HBA_GetRNIDMgmtInfo routine queries the HBA for request node identification data (RNID) management information. |
| [HBA_FreeLibrary function](nf-hbaapi-hba-freelibrary.md) | The HBA_FreeLibrary routine releases system resources associated with fibre channel HBA library. |
| [SMHBA_GetPhyStatistics function](nf-hbaapi-smhba-getphystatistics.md) | TBD |
| [HBA_GetFcpTargetMappingV2 function](nf-hbaapi-hba-getfcptargetmappingv2.md) | The HBA_GetFcpTargetMappingV2 routine retrieves the mappings between operating system and fibre channel protocol (FCP) identifiers for a set of targets that the HBA can enumerate on the indicated port. |
| [HBA_GetVendorLibraryAttributes function](nf-hbaapi-hba-getvendorlibraryattributes.md) | The HBA_GetVendorLibraryAttributes routine retrieves the vendor-specific attributes of the fibre channel HBA API library. |
| [HBA_SetRNIDMgmtInfo function](nf-hbaapi-hba-setrnidmgmtinfo.md) | The HBA_SetRNIDMgmtInfo routine programs the HBA to return the indicated request node identification information data (RNID). |
| [SMHBA_GetVersion function](nf-hbaapi-smhba-getversion.md) | TBD |
| [HBA_GetPersistentBindingV2 function](nf-hbaapi-hba-getpersistentbindingv2.md) | The HBA_GetPersistentBindingV2 routine retrieves persistent bindings, including extended bindings, for logical units that the HBA enumerates on the indicated port. |
| [HBA_GetAdapterPortAttributes function](nf-hbaapi-hba-getadapterportattributes.md) | The HBA_GetAdapterPortAttributes routine retrieves the attributes for a specified remote fibre channel port. |
| [SMHBA_SendTEST function](nf-hbaapi-smhba-sendtest.md) | TBD |
| [HBA_SendSRL function](nf-hbaapi-hba-sendsrl.md) | The HBA_SendSRL routine issues a scan remote loop (SRL) request through the specified HBA to a specified domain controller. |
| [HBA_SendRPL function](nf-hbaapi-hba-sendrpl.md) | The HBA_SendRPL routine sends a read port list (RPL) request to the indicated port or domain controller. |
| [HBA_RegisterForTargetEvents function](nf-hbaapi-hba-registerfortargetevents.md) | The HBA_RegisterForTargetEvents routine registers for target events with a specified target or with all targets associated with an adapter. |
| [HBA_GetFCPStatistics function](nf-hbaapi-hba-getfcpstatistics.md) | The HBA_GetFCPStatistics routine retrieves traffic statistics that the fibre channel protocol (FCP) has collected for the indicated logical unit. |
| [HBA_RegisterForAdapterEvents function](nf-hbaapi-hba-registerforadapterevents.md) | The HBA_RegisterForAdapterEvents routine registers the indicated user callback routine to call when an adapter event occurs. |
| [HBA_GetWrapperLibraryAttributes function](nf-hbaapi-hba-getwrapperlibraryattributes.md) | The HBA_GetWrapperLibraryAttributes routine retrieves the attributes of the fibre channel HBA API library that are operating system-specific. |
| [SMHBA_GetVendorLibraryAttributes function](nf-hbaapi-smhba-getvendorlibraryattributes.md) | TBD |
| [HBA_RegisterForAdapterAddEvents function](nf-hbaapi-hba-registerforadapteraddevents.md) | The HBA_RegisterForAdapterAddEvents routine registers the indicated user callback routine to call when a new adapter is added to the system. |
| [HBA_SendRPS function](nf-hbaapi-hba-sendrps.md) | The HBA_SendRPS routine sends a read port status block (RPS) request to the indicated agent port or domain controller. |
| [SMHBA_GetWrapperLibraryAttributes function](nf-hbaapi-smhba-getwrapperlibraryattributes.md) | TBD |
| [SMHBA_GetBindingSupport function](nf-hbaapi-smhba-getbindingsupport.md) | TBD |
| [SMHBA_GetLUNStatistics function](nf-hbaapi-smhba-getlunstatistics.md) | TBD |
| [SMHBA_GetFCPhyAttributes function](nf-hbaapi-smhba-getfcphyattributes.md) | TBD |
| [HBA_SendRNIDV2 function](nf-hbaapi-hba-sendrnidv2.md) | The HBA_SendRNIDV2 routine sends a request for node identification data (RNID) to the indicated HBA, which in turn routes the request through the indicated port or node to the appropriate fabric configuration server. |
| [HBA_SendScsiInquiry function](nf-hbaapi-hba-sendscsiinquiry.md) | The HBA_SendScsiInquiry routine sends a SCSI inquiry command to the indicated remote port. |
| [HBA_ScsiInquiryV2 function](nf-hbaapi-hba-scsiinquiryv2.md) | The HBA_ScsiInquiryV2 routine sends a SCSI inquiry command to the specified remote port. |
| [SMHBA_ScsiReadCapacity function](nf-hbaapi-smhba-scsireadcapacity.md) | TBD |
| [HBA_CloseAdapter function](nf-hbaapi-hba-closeadapter.md) | The HBA_CloseAdapter routine releases system resources associated with the indicated open HBA handle. |
| [HBA_ScsiReportLUNsV2 function](nf-hbaapi-hba-scsireportlunsv2.md) | The HBA_ScsiReportLUNsV2 routine sends a SCSI report LUNs command to the indicated remote port. |
| [HBA_GetPortAttributesByWWN function](nf-hbaapi-hba-getportattributesbywwn.md) | The HBA_GetPortAttributesByWWN routine retrieves the attributes for the port specified by the indicated port name. |
| [SMHBA_GetAdapterAttributes function](nf-hbaapi-smhba-getadapterattributes.md) | TBD |
| [HBA_GetBindingSupport function](nf-hbaapi-hba-getbindingsupport.md) | The HBA_GetBindingSupport routine retrieves the binding capabilities currently enabled for the specified port. |
| [SMHBA_GetPortAttributesByWWN function](nf-hbaapi-smhba-getportattributesbywwn.md) | TBD |
| [HBA_GetFcpTargetMapping function](nf-hbaapi-hba-getfcptargetmapping.md) | The HBA_GetFcpTargetMapping routine retrieves the mappings between operating system and fibre channel protocol (FCP) identifiers for a set of targets that the HBA can enumerate. |
| [HBA_SendRNID function](nf-hbaapi-hba-sendrnid.md) | The HBA_SendRNID routine sends a request for node identification data (RNID) to the indicated HBA, which in turn routes the request through the indicated port or node to the appropriate fabric configuration server. |
| [HBA_GetNumberOfAdapters function](nf-hbaapi-hba-getnumberofadapters.md) | The HBA_GetNumberOfAdapters routine returns the number of HBAs supported by the library. |
| [SMHBA_SendECHO function](nf-hbaapi-smhba-sendecho.md) | TBD |
| [SMHBA_ScsiInquiry function](nf-hbaapi-smhba-scsiinquiry.md) | TBD |
| [SMHBA_GetAdapterPortAttributes function](nf-hbaapi-smhba-getadapterportattributes.md) | TBD |
| [HBA_SetPersistentBindingV2 function](nf-hbaapi-hba-setpersistentbindingv2.md) | The HBA_SetPersistentBindingV2 routine establishes a set of bindings between operating system and fibre channel protocol (FCP) identifiers for the logical units that the HBA can enumerate on the specified port. |
| [HBA_GetBindingCapability function](nf-hbaapi-hba-getbindingcapability.md) | The HBA_GetBindingCapability routine retrieves the binding capabilities of the indicated port. |
| [SMHBA_GetPersistentBinding function](nf-hbaapi-smhba-getpersistentbinding.md) | TBD |
| [HBA_RegisterForAdapterPortEvents function](nf-hbaapi-hba-registerforadapterportevents.md) | The HBA_RegisterForAdapterPortEvents routine registers the indicated user callback routine to call when a port event occurs. |
| [HBA_SendRLS function](nf-hbaapi-hba-sendrls.md) | The HBA_SendRLS WMI routine sends a read link error status block (RLS) request through the indicated local port to the indicated remote port to retrieve a link error status block associated with the remote port. |
| [HBA_LoadLibrary function](nf-hbaapi-hba-loadlibrary.md) | The HBA_LoadLibrary routine loads and initializes the system-supplied fibre channel HBA API library. |
| [SMHBA_GetSASPhyAttributes function](nf-hbaapi-smhba-getsasphyattributes.md) | TBD |
| [SMHBA_RegisterForAdapterPhyStatEvents function](nf-hbaapi-smhba-registerforadapterphystatevents.md) | TBD |
| [HBA_GetSBTargetMapping function](nf-hbaapi-hba-getsbtargetmapping.md) | TBD |
| [SMHBA_GetDiscoveredPortAttributes function](nf-hbaapi-smhba-getdiscoveredportattributes.md) | TBD |
| [SMHBA_RemoveAllPersistentBindings function](nf-hbaapi-smhba-removeallpersistentbindings.md) | TBD |
| [HBA_GetAdapterName function](nf-hbaapi-hba-getadaptername.md) | The HBA_GetAdapterName routine retrieves the text string that identifies the HBA name that corresponds to the indicated adapter index. |
| [SMHBA_SetBindingSupport function](nf-hbaapi-smhba-setbindingsupport.md) | TBD |
| [HBA_GetAdapterAttributes function](nf-hbaapi-hba-getadapterattributes.md) | The HBA_GetAdapterAttributes routine retrieves the attributes for an HBA. |
| [HBA_GetFC4Statistics function](nf-hbaapi-hba-getfc4statistics.md) | The HBA_GetFC4Statistics routine retrieves traffic statistics that a specific FC-4 protocol has collected for the indicated port and local adapter. |
| [HBA_GetPortStatistics function](nf-hbaapi-hba-getportstatistics.md) | The HBA_GetPortStatistics routine retrieves statistics for the indicated port on the HBA. |
| [HBA_SendReportLUNs function](nf-hbaapi-hba-sendreportluns.md) | The HBA_SendReportLUNs routine sends a SCSI report LUNs command to the indicated remote port. |
| [HBA_GetDiscoveredPortAttributes function](nf-hbaapi-hba-getdiscoveredportattributes.md) | The HBA_GetDiscoveredPortAttributes routine retrieves the attributes for a specified remote fibre channel port. |
| [HBA_OpenAdapter function](nf-hbaapi-hba-openadapter.md) | The HBA_OpenAdapter routine opens an HBA and returns a handle. |
| [HBA_OpenAdapterByWWN function](nf-hbaapi-hba-openadapterbywwn.md) | The HBA_OpenAdapterByWWN routine opens the HBA that is associated with either a node or a port that has the indicated name. |
| [SMHBA_SetPersistentBinding function](nf-hbaapi-smhba-setpersistentbinding.md) | TBD |
| [HBA_SendCTPassThru function](nf-hbaapi-hba-sendctpassthru.md) | The HBA_SendCTPassThru routine sends a common transport (CT) pass-through command. |
| [HBA_RegisterForAdapterPortStatEvents function](nf-hbaapi-hba-registerforadapterportstatevents.md) | The HBA_RegisterForAdapterPortStatEvents routine registers the indicated user callback routine to call when a port statistics event occurs. |
| [HBA_ResetStatistics function](nf-hbaapi-hba-resetstatistics.md) | The HBA_ResetStatistics routine resets the statistics counters for the indicated port and HBA. |
| [HBA_SendCTPassThruV2 function](nf-hbaapi-hba-sendctpassthruv2.md) | The HBA_SendCTPassThruV2 routine sends a common transport (CT) pass-through command through the indicated port. |
| [SMHBA_RegisterForAdapterPortStatEvents function](nf-hbaapi-smhba-registerforadapterportstatevents.md) | TBD |
| [SMHBA_RemovePersistentBinding function](nf-hbaapi-smhba-removepersistentbinding.md) | TBD |
| [SMHBA_RegisterForAdapterAddEvents function](nf-hbaapi-smhba-registerforadapteraddevents.md) | TBD |
| [HBA_SBDskGetCapacity function](nf-hbaapi-hba-sbdskgetcapacity.md) | TBD |
| [HBA_RemovePersistentBinding function](nf-hbaapi-hba-removepersistentbinding.md) | The HBA_RemovePersistentBinding routine retrieves information about the specified target. |
| [SMHBA_GetProtocolStatistics function](nf-hbaapi-smhba-getprotocolstatistics.md) | TBD |
| [HBA_GetEventBuffer function](nf-hbaapi-hba-geteventbuffer.md) | The HBA_GetEventBuffer routine retrieves the indicated number of events, if available, from the HBA's event queue. |
| [HBA_RegisterLibrary function](nf-hbaapi-hba-registerlibrary.md) | TBD |
| [SMHBA_SendSMPPassThru function](nf-hbaapi-smhba-sendsmppassthru.md) | TBD |
| [SMHBA_GetPortType function](nf-hbaapi-smhba-getporttype.md) | TBD |
| [HBA_SendLIRR function](nf-hbaapi-hba-sendlirr.md) | The HBA_SendLIRR routine registers or de-registers a local (source) port to receive link incident records (LIR) from a remote (destination) port. |
| [HBA_ScsiReadCapacityV2 function](nf-hbaapi-hba-scsireadcapacityv2.md) | The HBA_ScsiReadCapacityV2 routine sends a SCSI read capacity command to the indicated remote port. |
| [SMHBA_RegisterForAdapterEvents function](nf-hbaapi-smhba-registerforadapterevents.md) | TBD |
| [HBA_RemoveAllPersistentBindings function](nf-hbaapi-hba-removeallpersistentbindings.md) | The HBA_RemoveAllPersistentBindings routine removes all persistent bindings for a specified HBA port. |
| [HBA_SetBindingSupport function](nf-hbaapi-hba-setbindingsupport.md) | The HBA_SetBindingSupport routine enables the indicated set of capabilities on the adapter. |
| [HBA_RegisterForLinkEvents function](nf-hbaapi-hba-registerforlinkevents.md) | The HBA_RegisterForLinkEvents routine registers with a specified adapter for asynchronous fabric link-level events. |
| [SMHBA_RegisterLibrary function](nf-hbaapi-smhba-registerlibrary.md) | TBD |
| [HBA_RemoveCallback function](nf-hbaapi-hba-removecallback.md) | The HBA_RemoveCallback routine de-registers a callback routine. |
| [SMHBA_RegisterForTargetEvents function](nf-hbaapi-smhba-registerfortargetevents.md) | TBD |
| [HBA_RegisterLibraryV2 function](nf-hbaapi-hba-registerlibraryv2.md) | TBD |
| [SMHBA_GetBindingCapability function](nf-hbaapi-smhba-getbindingcapability.md) | TBD |
| [HBA_RefreshAdapterConfiguration function](nf-hbaapi-hba-refreshadapterconfiguration.md) | The HBA_RefreshAdapterConfiguration routine refreshes the library's internally cached HBA data. |
| [HBA_GetFcpPersistentBinding function](nf-hbaapi-hba-getfcppersistentbinding.md) | The HBA_GetFcpPersistentBinding routine retrieves the persistent bindings that are associated with the logical units that the HBA can enumerate. |
| [SMHBA_GetNumberOfPorts function](nf-hbaapi-smhba-getnumberofports.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [HBA_wwntype enumeration](ne-hbaapi-hba-wwntype.md) | The HBA_wwntype enumerator indicates whether a worldwide name specifies a port or a node (machine). |
| [HBA_fcpbindingtype enumeration](ne-hbaapi-hba-fcpbindingtype.md) | TBD |

This header is used in these topics:

- [Storage](..content/_Storage)
