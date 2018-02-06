---
UID: NA:hbapiwmi
ms.assetid: 2d111291-ad47-3189-aac5-bdd3b2a649a6
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# hbapiwmi.h header



hbapiwmi.h contains the following programming interfaces:







## Structures
| Title | Description |
| ---- |:---- |
| [_AddLink_OUT](ns-hbapiwmi-_addlink_out.md) | The AddLink_OUT structure is used by an HBA miniport driver to report the status of a call to the AddLink WMI method. |
| [_AddPort_IN](ns-hbapiwmi-_addport_in.md) | The AddPort_IN structure is used by a WMI client to deliver the input parameter data of the AddPort WMI method to the HBA miniport driver. |
| [_AddPort_OUT](ns-hbapiwmi-_addport_out.md) | The AddPort_OUT structure is used by a WMI provider to report the output parameter data of the AddPort WMI method to the WMI client. |
| [_AddTarget_IN](ns-hbapiwmi-_addtarget_in.md) | The AddPort_IN structure is used by a WMI client to deliver the input parameter data of the AddTarget WMI method to the HBA miniport driver. |
| [_AddTarget_OUT](ns-hbapiwmi-_addtarget_out.md) | The AddTarget_OUT structure is used by a WMI provider to report the output parameter data of the AddTarget WMI method to the WMI client. |
| [_GetBindingCapability_IN](ns-hbapiwmi-_getbindingcapability_in.md) | The GetBindingCapability_IN structure is used by a WMI client to deliver the input parameter data of the GetBindingCapability WMI method to the HBA miniport driver. |
| [_GetBindingCapability_OUT](ns-hbapiwmi-_getbindingcapability_out.md) | The GetBindingCapability_OUT structure is used by a WMI provider to report the output parameter data of the GetBindingCapability WMI method to the WMI client. |
| [_GetBindingSupport_IN](ns-hbapiwmi-_getbindingsupport_in.md) | The GetBindingSupport_IN structure is used by a WMI client to deliver the input parameter data of the GetBindingSupport WMI method to the HBA miniport driver. |
| [_GetBindingSupport_OUT](ns-hbapiwmi-_getbindingsupport_out.md) | The GetBindingSupport_OUT structure is used by a WMI provider to report the output parameter data of the GetBindingSupport WMI method to the WMI client. |
| [_GetDiscoveredPortAttributes_IN](ns-hbapiwmi-_getdiscoveredportattributes_in.md) | The GetDiscoveredPortAttributes_IN structure is used to pass input parameter data to the GetDiscoveredPortAttributes WMI method. |
| [_GetDiscoveredPortAttributes_OUT](ns-hbapiwmi-_getdiscoveredportattributes_out.md) | The GetDiscoveredPortAttributes_OUT structure is used to report the output parameter data of the GetDiscoveredPortAttributes WMI method to the WMI client. |
| [_GetEventBuffer_OUT](ns-hbapiwmi-_geteventbuffer_out.md) | The GetEventBuffer_OUT structure is used to report the output parameter data of the GetEventBuffer WMI method to the WMI client. |
| [_GetFC3MgmtInfo_OUT](ns-hbapiwmi-_getfc3mgmtinfo_out.md) | The GetFC3MgmtInfo_OUT structure is used to report the output parameter data of the GetFC3MgmtInfo WMI method to the WMI client. |
| [_GetFC4Statistics_IN](ns-hbapiwmi-_getfc4statistics_in.md) | The GetFC4Statistics_IN structure is used to pass input parameter data to the GetFC4Statistics WMI method. |
| [_GetFC4Statistics_OUT](ns-hbapiwmi-_getfc4statistics_out.md) | The GetFC4Statistics_OUT structure is used to report the output parameter data of the GetFC4Statistics WMI method to the WMI client. |
| [_GetFcpPersistentBinding_IN](ns-hbapiwmi-_getfcppersistentbinding_in.md) | The GetFcpPersistentBinding_IN structure is used to pass input parameter data to the GetFcpPersistentBinding WMI method |
| [_GetFcpPersistentBinding_OUT](ns-hbapiwmi-_getfcppersistentbinding_out.md) | The GetFcpPersistentBinding_OUT structure is used to report the output parameter data of the GetFcpPersistentBinding WMI method to the WMI client. |
| [_GetFCPStatistics_IN](ns-hbapiwmi-_getfcpstatistics_in.md) | The GetFCPStatistics_IN structure is used to deliver input parameter data to the GetFCPStatistics WMI method. |
| [_GetFCPStatistics_OUT](ns-hbapiwmi-_getfcpstatistics_out.md) | The GetFCPStatistics_OUT structure is used by the miniport driver to report the output parameters of the GetFCPStatistics WMI method. |
| [_GetFcpTargetMapping_IN](ns-hbapiwmi-_getfcptargetmapping_in.md) | The GetFcpTargetMapping_IN structure is used to report the output parameter data of the GetFcpTargetMapping WMI method to the WMI client. |
| [_GetFcpTargetMapping_OUT](ns-hbapiwmi-_getfcptargetmapping_out.md) | The GetFcpTargetMapping_OUT structure is used to report the output parameter data of the GetFcpTargetMapping WMI method to the WMI client. |
| [_GetPersistentBinding2_IN](ns-hbapiwmi-_getpersistentbinding2_in.md) | The GetPersistentBinding2_IN structure is used to deliver input parameter data to the GetPersistentBinding2 WMI method. |
| [_GetPersistentBinding2_OUT](ns-hbapiwmi-_getpersistentbinding2_out.md) | The GetBindingSupport_OUT structure is used to report the output parameter data of the GetPersistentBinding2 WMI method to the WMI client. |
| [_GetPortAttributesByWWN_IN](ns-hbapiwmi-_getportattributesbywwn_in.md) | The GetPortAttributesByWWN_IN structure is used by a WMI client to deliver input parameter data to the GetPortAttributesByWWN WMI method. |
| [_GetPortAttributesByWWN_OUT](ns-hbapiwmi-_getportattributesbywwn_out.md) | The GetPortAttributesByWWN_OUT structure is used to report the output parameter data of the GetPortAttributesByWWN WMI method to the WMI client. |
| [_HBAFC3MgmtInfo](ns-hbapiwmi-_hbafc3mgmtinfo.md) | The HBAFC3MgmtInfo structure is used to report FC3 management information associated with a fibre channel adapter. |
| [_HBAFCPBindingEntry](ns-hbapiwmi-_hbafcpbindingentry.md) | The HBAFCPBindingEntry structure defines a binding between the information that uniquely identifies a logical unit for the operating system and the fibre channel protocol (FCP) identifier for the logical unit. |
| [_HBAFCPBindingEntry2](ns-hbapiwmi-_hbafcpbindingentry2.md) | The HBAFCPBindingEntry2 structure defines a binding between the information that uniquely identifies a logical unit for the operating system and the fibre channel protocol (FCP) identifier for the logical unit. |
| [_HBAFCPID](ns-hbapiwmi-_hbafcpid.md) | The HBAFCPID structure contains information that uniquely identifies a logical unit on a fibre channel network. |
| [_HBAFCPScsiEntry](ns-hbapiwmi-_hbafcpscsientry.md) | The HBAFCPScsiEntry structure is used with GetFcpTargetMapping method of the MSFC_HBAFCPInfo WMI Class to define a binding between the operating system information that uniquely identifies a logical unit and the fibre channel protocol (FCP) identifier that identifies the logical unit. |
| [_HBAScsiID](ns-hbapiwmi-_hbascsiid.md) | The HBAScsiID structure contains information generated by the operating system that uniquely identifies a logical unit. |
| [_MS_SM_AdapterInformationQuery](ns-hbapiwmi-_ms_sm_adapterinformationquery.md) | The MS_SM_AdapterInformationQuery structure is used by a WMI provider to expose attributes that are associated with a SAS adapter. |
| [_MS_SMHBA_FC_PHY](ns-hbapiwmi-_ms_smhba_fc_phy.md) | The MS_SMHBA_FC_PHY structure is used to report the physical attributes of a fibre channel port. |
| [_MS_SMHBA_FC_Port](ns-hbapiwmi-_ms_smhba_fc_port.md) | The MS_SMHBA_FC_Port structure is used to report the FC port information. |
| [_MS_SMHBA_PORTATTRIBUTES](ns-hbapiwmi-_ms_smhba_portattributes.md) | The MS_SMHBA_PORTATTRIBUTES structure is used to report the port information. |
| [_MS_SMHBA_PORTLUN](ns-hbapiwmi-_ms_smhba_portlun.md) | The MS_SMHBA_PORTLUN structure reports target LUN information that is associated with a port. |
| [_MS_SMHBA_PROTOCOLSTATISTICS](ns-hbapiwmi-_ms_smhba_protocolstatistics.md) | The MS_SMHBA_PROTOCOLSTATISTICS structure is used to report protocol traffic statistics on a port. |
| [_MS_SMHBA_SAS_PHY](ns-hbapiwmi-_ms_smhba_sas_phy.md) | The MS_SMHBA_SAS_PHY structure is used to report the SAS physical port information. |
| [_MS_SMHBA_SAS_Port](ns-hbapiwmi-_ms_smhba_sas_port.md) | The MS_SMHBA_SAS_Port structure is used to report the SAS port information. |
| [_MS_SMHBA_SASPHYSTATISTICS](ns-hbapiwmi-_ms_smhba_sasphystatistics.md) | The MS_SMHBA_SASPHYSTATISTICS structure reports the traffic statistics for a SAS physical link. |
| [_MS_SMHBA_SCSIENTRY](ns-hbapiwmi-_ms_smhba_scsientry.md) | The MS_SMHBA_SCSIENTRY structure is used to report target LUN mapping information. |
| [_MSFC_AdapterEvent](ns-hbapiwmi-_msfc_adapterevent.md) | The MSFC_AdapterEvent structure is used by HBA miniport drivers that support the T11 committee's Fibre Channel HBA API specification to report adapter events to WMI clients that have registered to be notified of these events. |
| [_MSFC_EventBuffer](ns-hbapiwmi-_msfc_eventbuffer.md) | The MSFC_EventBuffer structure is used in conjunction with the GetEventBuffer method to retrieve the next events in the HBA's event queue. |
| [_MSFC_FC4STATISTICS](ns-hbapiwmi-_msfc_fc4statistics.md) | The MSFC_FC4STATISTICS structure is used in conjunction with the GetFC4Statistics WMI method to report traffic statistics on a port of type Nx_Port for the indicated FC-4 protocol. |
| [_MSFC_FCAdapterHBAAttributes](ns-hbapiwmi-_msfc_fcadapterhbaattributes.md) | The MSFC_FCAdapterHBAAttributes structure is used by a WMI provider to expose attribute information associated with a fibre channel adapter. |
| [_MSFC_FibrePortHBAAttributes](ns-hbapiwmi-_msfc_fibreporthbaattributes.md) | A WMI provider uses the MSFC_FibrePortHBAAttributes WMI class to expose attribute information associated with a fibre channel port. |
| [_MSFC_FibrePortHBAStatistics](ns-hbapiwmi-_msfc_fibreporthbastatistics.md) | The MSFC_FibrePortHBAStatistics structure is used by an HBA miniport driver that is a WMI provider to report statistics related to a fibre channel port. |
| [_MSFC_HBAPortAttributesResults](ns-hbapiwmi-_msfc_hbaportattributesresults.md) | The structure is used by the GetDiscoveredPortAttributes WMI method to report the attributes for a specified remote fibre channel port. |
| [_MSFC_HBAPortStatistics](ns-hbapiwmi-_msfc_hbaportstatistics.md) | The MSFC_HBAPortStatistics structure contains statistics information about a port. |
| [_MSFC_LinkEvent](ns-hbapiwmi-_msfc_linkevent.md) | A WMI provider uses the MSFC_LinkEvent structure to report link events for the indicated adapter. |
| [_MSFC_PortEvent](ns-hbapiwmi-_msfc_portevent.md) | A WMI provider uses the MSFC_PortEvent structure to report port events for the indicated adapter. |
| [_MSFC_TargetEvent](ns-hbapiwmi-_msfc_targetevent.md) | A WMI provider uses the MSFC_TargetEvent structure to report port events for the indicated adapter. |
| [_MSFC_TM](ns-hbapiwmi-_msfc_tm.md) | The MSFC_TM structure is used by WMI providers to timestamp events. |
| [_RemoveLink_OUT](ns-hbapiwmi-_removelink_out.md) | The RemoveLink_OUT structure is used by an HBA miniport driver to report the output parameter data of the RemoveLink WMI method to the WMI client. |
| [_RemovePersistentEntry_IN](ns-hbapiwmi-_removepersistententry_in.md) | The RemovePersistentEntry_IN structure is used by a WMI client to deliver input parameter data to the RemovePersistentEntry WMI method. |
| [_RemovePersistentEntry_OUT](ns-hbapiwmi-_removepersistententry_out.md) | The RemovePersistentEntry_OUT structure is used to report the output parameter data of the RemovePersistentEntry WMI method to the WMI client. |
| [_RemovePort_IN](ns-hbapiwmi-_removeport_in.md) | The Remove_IN structure is used by a WMI client to deliver input parameter data to the RemovePort WMI method. |
| [_RemovePort_OUT](ns-hbapiwmi-_removeport_out.md) | The RemovePort_OUT structure is used by an HBA miniport driver to the output parameter data of the RemovePort WMI method to the WMI client. |
| [_RemoveTarget_IN](ns-hbapiwmi-_removetarget_in.md) | The RemoveTarget_IN structure is used by a WMI client to deliver input parameter data to the RemoveTarget WMI method. |
| [_RemoveTarget_OUT](ns-hbapiwmi-_removetarget_out.md) | The RemoveTarget_OUT structure is used by an HBA miniport driver to report the output parameter data of the RemoveTarget WMI method to the WMI client. |
| [_ScsiInquiry_IN](ns-hbapiwmi-_scsiinquiry_in.md) | The ScsiInquiry_IN structure is used by a miniport driver to deliver input parameter data to the ScsiInquiry WMI method. |
| [_ScsiInquiry_OUT](ns-hbapiwmi-_scsiinquiry_out.md) | The ScsiInquiry_OUT structure is used to report the output data of the ScsiInquiry WMI method to the WMI client. |
| [_ScsiReadCapacity_IN](ns-hbapiwmi-_scsireadcapacity_in.md) | The ScsiReadCapacity_IN structure is used to deliver input parameter data to the ScsiReadCapacity WMI method. |
| [_ScsiReadCapacity_OUT](ns-hbapiwmi-_scsireadcapacity_out.md) | The ScsiReadCapacity_OUT structure is used to report the output data of the ScsiReadCapacity WMI method to the WMI client. |
| [_ScsiReportLuns_IN](ns-hbapiwmi-_scsireportluns_in.md) | The ScsiReportLuns_IN structure is used to deliver input parameter data to the ScsiReportLuns WMI method. |
| [_ScsiReportLuns_OUT](ns-hbapiwmi-_scsireportluns_out.md) | The ScsiReportLuns_OUT structure is used to report the output parameter data of the ScsiReportLuns WMI method to the WMI client. |
| [_SendCTPassThru_IN](ns-hbapiwmi-_sendctpassthru_in.md) | The SendCTPassThru_IN structure is used to deliver input parameter data to the SendCTPassThru WMI method. |
| [_SendCTPassThru_OUT](ns-hbapiwmi-_sendctpassthru_out.md) | The SendCTPassThru_OUT structure is used to report the output parameter data of the SendCTPassThru WMI method to the WMI client. |
| [_SendLIRR_IN](ns-hbapiwmi-_sendlirr_in.md) | The SendLIRR_IN structure is used to deliver parameter data to the SendLIRR WMI method. |
| [_SendLIRR_OUT](ns-hbapiwmi-_sendlirr_out.md) | The SendLIRR_OUT structure is used to report the output parameter data of the SendLIRR WMI method to the WMI client. |
| [_SendRLS_IN](ns-hbapiwmi-_sendrls_in.md) | The SendRLS_IN structure is used to deliver input parameter data to the SendRLS WMI method. |
| [_SendRLS_OUT](ns-hbapiwmi-_sendrls_out.md) | The SendRLS_OUT structure is used to report the output parameter data of the SendRLS WMI method to the WMI client. |
| [_SendRNID_IN](ns-hbapiwmi-_sendrnid_in.md) | The SendRNID_IN structure is used to deliver input parameter data to the SendRNID WMI method. |
| [_SendRNID_OUT](ns-hbapiwmi-_sendrnid_out.md) | The SendRNID_OUT structure is used to report the output parameter data of the SendRNID WMI method to the WMI client. |
| [_SendRNIDV2_IN](ns-hbapiwmi-_sendrnidv2_in.md) | The SendRNIDV2_IN structure is used to deliver input parameter data to the SendRNIDV2 WMI method. |
| [_SendRNIDV2_OUT](ns-hbapiwmi-_sendrnidv2_out.md) | The SendRNIDV2_OUT structure is used to report the output parameter data of the SendRNIDV2 WMI method to the WMI client. |
| [_SendRPL_IN](ns-hbapiwmi-_sendrpl_in.md) | The SendRPL_IN structure is used to deliver input parameter data to the SendRPL WMI method. |
| [_SendRPL_OUT](ns-hbapiwmi-_sendrpl_out.md) | The SendRPL_OUT structure is used to report the output parameter data of the SendRPL WMI method to the WMI client. |
| [_SendRPS_IN](ns-hbapiwmi-_sendrps_in.md) | The SendRPS_IN structure is used to deliver input parameter data to the SendRPS WMI method. |
| [_SendRPS_OUT](ns-hbapiwmi-_sendrps_out.md) | The SendRPS_OUT structure is used to report the output parameter data of the SendRPS WMI method to the WMI client. |
| [_SendSRL_OUT](ns-hbapiwmi-_sendsrl_out.md) | The SendSRL_OUT structure is used to report the output parameter data of the SendSRL WMI method to the WMI client. |
| [_SetBindingSupport_IN](ns-hbapiwmi-_setbindingsupport_in.md) | The SetBindingSupport_IN structure is used to deliver input parameter data to the SetBindingSupport WMI method. |
| [_SetBindingSupport_OUT](ns-hbapiwmi-_setbindingsupport_out.md) | The SetBindingSupport_OUT structure is used to report the output parameter data of the SetBindingSupport WMI method to the WMI client. |
| [_SetFC3MgmtInfo_IN](ns-hbapiwmi-_setfc3mgmtinfo_in.md) | The SetFC3MgmtInfo_IN structure is used to deliver input parameter data to the SetFC3MgmtInfo WMI method. |
| [_SetFC3MgmtInfo_OUT](ns-hbapiwmi-_setfc3mgmtinfo_out.md) | The SetFC3MgmtInfo_OUT structure is used to report the output parameter data of the SetFC3MgmtInfo WMI method to the WMI client. |
| [_SetPersistentEntry_IN](ns-hbapiwmi-_setpersistententry_in.md) | The SetPersistentEntry_IN structure is used by a WMI client to deliver the input parameter data of the SetPersistentEntry WMI method to the HBA miniport driver. |
| [_SetPersistentEntry_OUT](ns-hbapiwmi-_setpersistententry_out.md) | The SetPersistentEntry_OUT structure is used to report the output parameter data of the SetPersistentEntry WMI method to the WMI client. |
| [_SM_AddLink_OUT](ns-hbapiwmi-_sm_addlink_out.md) | The SM_AddLink_OUT structure is used to receive output parameters from the SM_AddLink WMI method. |
| [_SM_AddPort_IN](ns-hbapiwmi-_sm_addport_in.md) | The SM_AddPort_IN structure is used to provide input parameters to the SM_AddPort WMI method. |
| [_SM_AddPort_OUT](ns-hbapiwmi-_sm_addport_out.md) | The SM_AddPort_OUT structure is used to receive output parameters from the SM_RemoveTarget WMI method. |
| [_SM_AddTarget_IN](ns-hbapiwmi-_sm_addtarget_in.md) | The SM_AddTarget_IN structure is used to provide input parameters to the SM_AddTarget WMI method. |
| [_SM_AddTarget_OUT](ns-hbapiwmi-_sm_addtarget_out.md) | The SM_AddTarget_OUT structure is used to receive output parameters from the SM_AddTarget WMI method. |
| [_SM_GetBindingCapability_IN](ns-hbapiwmi-_sm_getbindingcapability_in.md) | The SM_GetBindingCapability_IN structure is used to provide input parameters to the SM_GetBindingCapability method. |
| [_SM_GetBindingCapability_OUT](ns-hbapiwmi-_sm_getbindingcapability_out.md) | The SM_GetBindingCapability_OUT structure is used to receive output parameters from the SM_GetBindingCapability method. |
| [_SM_GetBindingSupport_IN](ns-hbapiwmi-_sm_getbindingsupport_in.md) | The SM_GetBindingSupport_IN structure is used to provide input parameters to the SM_GetBindingSupport method. |
| [_SM_GetBindingSupport_OUT](ns-hbapiwmi-_sm_getbindingsupport_out.md) | The SM_GetBindingSupport_OUT structure is used to receive output parameters from the SM_GetBindingSupport method. |
| [_SM_GetLUNStatistics_IN](ns-hbapiwmi-_sm_getlunstatistics_in.md) | The SM_GetLUNStatistics_IN structure is used to provide input parameters to the SM_GetLUNStatistics_IN method. |
| [_SM_GetLUNStatistics_OUT](ns-hbapiwmi-_sm_getlunstatistics_out.md) | The SM_GetLUNStatistics_OUT structure is used to receive output parameters from the SM_GetLUNStatistics_OUT method. |
| [_SM_GetPersistentBinding_IN](ns-hbapiwmi-_sm_getpersistentbinding_in.md) | The SM_GetPersistentBinding_IN structure is used to provide input parameters to the SM_GetPersistentBinding method. |
| [_SM_GetPersistentBinding_OUT](ns-hbapiwmi-_sm_getpersistentbinding_out.md) | The SM_GetPersistentBinding_OUT structure is used to receive output parameters from the SM_GetPersistentBinding method. |
| [_SM_GetRNIDMgmtInfo_OUT](ns-hbapiwmi-_sm_getrnidmgmtinfo_out.md) | The SM_GetRNIDMgmtInfo_OUT structure is used to receive output parameters from the SM_GetRNIDMgmtInfo method. |
| [_SM_GetTargetMapping_IN](ns-hbapiwmi-_sm_gettargetmapping_in.md) | The SM_GetTargetMapping_IN structure is used to provide input parameters to the SM_GetTargetMapping method. |
| [_SM_GetTargetMapping_OUT](ns-hbapiwmi-_sm_gettargetmapping_out.md) | The SM_GetTargetMapping structure_OUT structure is used to receive output parameters from the SM_GetTargetMapping method. |
| [_SM_RemoveLink_OUT](ns-hbapiwmi-_sm_removelink_out.md) | The SM_RemoveLink_OUT structure is used to receive output parameters from the SM_RemoveLink WMI method. |
| [_SM_RemovePersistentBinding_IN](ns-hbapiwmi-_sm_removepersistentbinding_in.md) | The SM_RemovePersistentBinding_IN structure is used to provide input parameters to the SM_RemovePersistentBinding method. |
| [_SM_RemovePersistentBinding_OUT](ns-hbapiwmi-_sm_removepersistentbinding_out.md) | The SM_REmovePersistentBinding_OUT structure is used to receive output parameters from the SM_RemovePersistentBinding method. |
| [_SM_RemovePort_IN](ns-hbapiwmi-_sm_removeport_in.md) | The SM_RemovePort_IN structure is used to provide input parameters to the SM_RemovePort WMI method. |
| [_SM_RemovePort_OUT](ns-hbapiwmi-_sm_removeport_out.md) | The SM_RemovePort_OUT structure is used to receive output parameters from the SM_RemovePort WMI method. |
| [_SM_RemoveTarget_IN](ns-hbapiwmi-_sm_removetarget_in.md) | The SM_RemoveTarget_IN structure is used to provide input parameters to the SM_RemoveTarget WMI method. |
| [_SM_RemoveTarget_OUT](ns-hbapiwmi-_sm_removetarget_out.md) | The SM_RemoveTarget_OUT structure is used to receive output parameters from the SM_RemoveTarget WMI method. |
| [_SM_SendCTPassThru_IN](ns-hbapiwmi-_sm_sendctpassthru_in.md) | The SM_SendCTPassThru_IN structure is used to provide input parameters to the SM_SendCTPassThru method. |
| [_SM_SendCTPassThru_OUT](ns-hbapiwmi-_sm_sendctpassthru_out.md) | The SM_SendCTPassThru_OUT structure is used to receive output parameters from the SM_SendCTPassThru method. |
| [_SM_SendECHO_IN](ns-hbapiwmi-_sm_sendecho_in.md) | The SM_SendECHO_IN structure is used to provide input parameters to the SM_SendECHO method. |
| [_SM_SendECHO_OUT](ns-hbapiwmi-_sm_sendecho_out.md) | The SM_SendECHO_OUT structure is used to receive output parameters from the SM_SendECHO method. |
| [_SM_SendLIRR_OUT](ns-hbapiwmi-_sm_sendlirr_out.md) | The SM_SendLIRR_OUT structure is used to receive output parameters from the SM_SendLIRR method. |
| [_SM_SendRLS_OUT](ns-hbapiwmi-_sm_sendrls_out.md) | The SM_SendRLS_OUT structure is used to receive output parameters from the SM_SendRLS method. |
| [_SM_SendRNID_IN](ns-hbapiwmi-_sm_sendrnid_in.md) | The SM_SendRNID_IN structure is used to provide input parameters to the SM_SendRNID method. |
| [_SM_SendRNID_OUT](ns-hbapiwmi-_sm_sendrnid_out.md) | The SM_SendRNID_OUT structure is used to receive output parameters from the SM_SendRNID method. |
| [_SM_SendRPL_IN](ns-hbapiwmi-_sm_sendrpl_in.md) | The SM_SendRPL_IN structure is used to provide input parameters to the SM_SendRPL method. |
| [_SM_SendRPL_OUT](ns-hbapiwmi-_sm_sendrpl_out.md) | The SM_SendRPL_OUT structure is used to receive output parameters from the SM_SendRPL method. |
| [_SM_SendRPS_OUT](ns-hbapiwmi-_sm_sendrps_out.md) | The SM_SendRPS_OUT structure is used to receive output parameters from the SM_SendRPS method. |
| [_SM_SendSMPPassThru_OUT](ns-hbapiwmi-_sm_sendsmppassthru_out.md) | The SM_SendSMPPassThru_OUT structure is used to receive output parameters from the SM_SendSMPPassThru method. |
| [_SM_SendSRL_OUT](ns-hbapiwmi-_sm_sendsrl_out.md) | The SM_SendSRL_OUT structure is used to receive output parameters from the SM_SendSRL method. |
| [_SM_SendTEST_IN](ns-hbapiwmi-_sm_sendtest_in.md) | The SM_SendTEST_IN structure is used to provide input parameters to the SM_SendTEST method. |
| [_SM_SendTEST_OUT](ns-hbapiwmi-_sm_sendtest_out.md) | The SM_SendTEST_OUT structure is used to receive output parameters from the SM_SendTEST method. |
| [_SM_SetBindingSupport_IN](ns-hbapiwmi-_sm_setbindingsupport_in.md) | The SM_SetBindingSupport_IN structure is used to provide input parameters to the SM_SetBindingSupport method. |
| [_SM_SetBindingSupport_OUT](ns-hbapiwmi-_sm_setbindingsupport_out.md) | The SM_SetBindingSupport_OUT structure is used to receive output parameters from the SM_SetBindingSupport method. |
| [_SM_SetPersistentBinding_IN](ns-hbapiwmi-_sm_setpersistentbinding_in.md) | The SM_SetPersistentBinding_IN structure is used to provide input parameters to the SM_SetPersistentBinding method. |
| [_SM_SetPersistentBinding_OUT](ns-hbapiwmi-_sm_setpersistentbinding_out.md) | The SM_SetPersistentBinding_OUT structure is used to receive output parameters from the SM_SetPersistentBinding method. |
| [_SM_SetRNIDMgmtInfo_IN](ns-hbapiwmi-_sm_setrnidmgmtinfo_in.md) | The SM_SetRNIDMgmtInfo_IN structure is used to provide input parameters to the SM_SetRNIDMgmtInfo method. |
| [_SM_SetRNIDMgmtInfo_OUT](ns-hbapiwmi-_sm_setrnidmgmtinfo_out.md) | The SM_SetRNIDMgmtInfo_OUT structure is used to receive output parameters from the SM_SetRNIDMgmtInfo method. |