# Iscsiop.h header


This header is used by unknown technology.

Iscsiop.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [AddConnectionToSession_IN structure](ns-iscsiop--addconnectiontosession-in.md) | The AddConnectionToSession_IN structure holds input data for the AddConnectionToSession method, which is used to add a new connection to an already existing session. |
| [AddConnectionToSession_OUT structure](ns-iscsiop--addconnectiontosession-out.md) | The AddConnectionToSession_OUT structure holds output data for the AddConnectionToSession method. |
| [AddRADIUSServer_IN structure](ns-iscsiop--addradiusserver-in.md) | The AddRADIUSServer_IN structure holds the input data for the AddRADIUSServer method, which is used to add a new RADIUS server entry to existing list. |
| [AddRADIUSServer_OUT structure](ns-iscsiop--addradiusserver-out.md) | The AddRADIUSServer_OUT structure holds the output data for the AddRADIUSServer method. |
| [AddiSNSServer_IN structure](ns-iscsiop--addisnsserver-in.md) | The AddiSNSServer_IN structure holds the input data for the user-mode AddISNSServer method, which is used to add a new iSNS server entry to the list of iSNS server names that the initiator maintains. |
| [AddiSNSServer_OUT structure](ns-iscsiop--addisnsserver-out.md) | The AddiSNSServer_OUT structure holds the output data for the user-mode AddISNSServer method. |
| [ClearCache_OUT structure](ns-iscsiop--clearcache-out.md) | The ClearCache_OUT structure holds the output data for the ClearCache method. |
| [DeleteInitiatorNodeName_IN structure](ns-iscsiop--deleteinitiatornodename-in.md) | The DeleteInitiatorNodeName_IN structure holds the input data for the DeleteInitiatorNodeName method, which is used to delete an initiator node name. |
| [DeleteInitiatorNodeName_OUT structure](ns-iscsiop--deleteinitiatornodename-out.md) | The DeleteInitiatorNodeName_OUT structure holds the output data for the DeleteInitiatorNodeName method. |
| [GetPresharedKeyForId_IN structure](ns-iscsiop--getpresharedkeyforid-in.md) | The GetPresharedKeyForId_IN structure holds the input data for the GetPresharedKeyForId method. |
| [GetPresharedKeyForId_OUT structure](ns-iscsiop--getpresharedkeyforid-out.md) | The GetPresharedKeyForId_OUT structure holds the output data for the GetPresharedKeyForId method. |
| [ISCSI_Persistent_Login structure](ns-iscsiop--iscsi-persistent-login.md) | The ISCSI_Persistent_Login structure defines a persistent logon that the operating system initiates automatically when the computer boots up. |
| [LoginToTarget_IN structure](ns-iscsiop--logintotarget-in.md) | The LoginToTarget_IN structure holds the input data for the LoginToTarget method, which is used to login to a target. |
| [LoginToTarget_OUT structure](ns-iscsiop--logintotarget-out.md) | The LoginToTarget_OUT structure holds the output data for the LoginToTarget method. |
| [LogoutFromTarget_IN structure](ns-iscsiop--logoutfromtarget-in.md) | The LogoutFromTarget_IN structure holds the input data for the LogoutFromTarget method, which is used to log out from an iSCSI target. |
| [LogoutFromTarget_OUT structure](ns-iscsiop--logoutfromtarget-out.md) | The LogoutFromTarget_OUT structure holds the output data for the LogoutFromTarget method. |
| [MSiSCSI_AdapterEvent structure](ns-iscsiop--msiscsi-adapterevent.md) | The MSiSCSI_AdapterEvent structure contains information that is reported whenever an adapter event occurs. |
| [MSiSCSI_BootInformation structure](ns-iscsiop--msiscsi-bootinformation.md) | The MSiSCSI_BootInformation structure is used with the MSiSCSI_BootInformation WMI Class to expose information about the node that contains the target boot device. |
| [MSiSCSI_LUNMappingInformation structure](ns-iscsiop--msiscsi-lunmappinginformation.md) | This MSiSCSI_LUNMappingInformation structure provides the SCSI address information that the operating system assigns to a particular logical unit. |
| [MSiSCSI_PersistentLogins structure](ns-iscsiop--msiscsi-persistentlogins.md) | The MSiSCSI_PersistentLogins structure contains the list of persistent target logon sessions. |
| [MSiSCSI_TargetMappings structure](ns-iscsiop--msiscsi-targetmappings.md) | The MSiSCSI_TargetMappings structure contains a set of logical unit number (LUN) mappings that are associated with an initiator instance. |
| [RemoveConnectionFromSession_IN structure](ns-iscsiop--removeconnectionfromsession-in.md) | The RemoveConnectionFromSession_IN structure holds the input data for the RemoveConnectionFromSession method, which is used to remove a connection from a session. |
| [RemoveConnectionFromSession_OUT structure](ns-iscsiop--removeconnectionfromsession-out.md) | The RemoveConnectionFromSession_OUT structure holds the output data for the RemoveConnectionFromSession method, which is used to remove a connection from a session. |
| [RemovePersistentLogin_IN structure](ns-iscsiop--removepersistentlogin-in.md) | The RemovePersistentLogin_IN structure holds the input data for the RemovePersistentLogin method, which is used to remove persistent login information. |
| [RemovePersistentLogin_OUT structure](ns-iscsiop--removepersistentlogin-out.md) | The RemovePersistentLogin_OUT structure holds the output data for the RemovePersistentLogin method. |
| [RemoveRADIUSServer_IN structure](ns-iscsiop--removeradiusserver-in.md) | The RemoveRADIUSServer_IN structure holds the input data for the user-mode RemoveRADIUSServer method, which is used to remove a RADIUS server entry. |
| [RemoveRADIUSServer_OUT structure](ns-iscsiop--removeradiusserver-out.md) | The RemoveiSNSServer_OUT structure holds the output data for the RemoveRADIUSServer method. |
| [RemoveiSNSServer_IN structure](ns-iscsiop--removeisnsserver-in.md) | The RemoveiSNSServer_IN structure holds the input data for the user-mode RemoveISNSServer method, which is used to remove an iSNS server entry. |
| [RemoveiSNSServer_OUT structure](ns-iscsiop--removeisnsserver-out.md) | The RemoveiSNSServer_OUT structure holds the output data for the user-mode RemoveISNSServer method. |
| [ScsiInquiry_IN structure](ns-iscsiop--scsiinquiry-in.md) | The ScsiInquiry_IN structure holds the input data for the ScsiInquiry method, which is used to send a SCSI inquiry command. |
| [ScsiInquiry_OUT structure](ns-iscsiop--scsiinquiry-out.md) | The ScsiInquiry_OUT structure holds the output data for the ScsiInquiry method. |
| [ScsiReadCapacity_IN structure](ns-iscsiop--scsireadcapacity-in.md) | The ScsiReadCapacity_IN structure holds the input data for the ScsiReadCapacity method, which is used to send a SCSI read Ccapacity command. |
| [ScsiReadCapacity_OUT structure](ns-iscsiop--scsireadcapacity-out.md) | The ScsiReadCapacity_OUT structure holds the output data for the ScsiReadCapacity method. |
| [ScsiReportLuns_IN structure](ns-iscsiop--scsireportluns-in.md) | The ScsiReportLuns_IN structure holds the input data for the ScsiReportLuns method. |
| [ScsiReportLuns_OUT structure](ns-iscsiop--scsireportluns-out.md) | The ScsiReportLuns_OUT structure holds the output data for the ScsiReportLuns method. |
| [SendTargets_IN structure](ns-iscsiop--sendtargets-in.md) | The SendTargets_IN structure holds the input data for the SendTargets method. |
| [SendTargets_OUT structure](ns-iscsiop--sendtargets-out.md) | The SendTargets_OUT structure holds the output data for the SendTargets method. |
| [SetCHAPSharedSecret_IN structure](ns-iscsiop--setchapsharedsecret-in.md) | The SetCHAPSharedSecret_IN structure holds the input data for the SetCHAPSharedSecret method. |
| [SetCHAPSharedSecret_OUT structure](ns-iscsiop--setchapsharedsecret-out.md) | The SetCHAPSharedSecret_OUT structure holds the output data for the SetCHAPSharedSecret method. |
| [SetGenerationalGuid_IN structure](ns-iscsiop--setgenerationalguid-in.md) | The SetGenerationalGuid_IN structure holds the input data for the SetGenerationalGuid method. |
| [SetGenerationalGuid_OUT structure](ns-iscsiop--setgenerationalguid-out.md) | The SetGenerationalGuid_OUT structure holds the output data for the SetGenerationalGuid method. |
| [SetGroupPresharedKey_IN structure](ns-iscsiop--setgrouppresharedkey-in.md) | The SetGroupPresharedKey_IN structure holds the input data for the SetGroupPresharedKey method. |
| [SetGroupPresharedKey_OUT structure](ns-iscsiop--setgrouppresharedkey-out.md) | The SetGroupPresharedKey_OUT structure holds the output data for the SetGroupPresharedKey method. |
| [SetInitiatorNodeName_IN structure](ns-iscsiop--setinitiatornodename-in.md) | The SetInitiatorNodeName_IN structure holds the input data for the SetInitiatorNodeName method. |
| [SetInitiatorNodeName_OUT structure](ns-iscsiop--setinitiatornodename-out.md) | The SetInitiatorNodeName_OUT structure holds the output data for the SetInitiatorNodeName method. |
| [SetPresharedKeyForId_IN structure](ns-iscsiop--setpresharedkeyforid-in.md) | The SetPresharedKeyForId_IN structure holds the input data for the SetPresharedKeyForId method. |
| [SetPresharedKeyForId_OUT structure](ns-iscsiop--setpresharedkeyforid-out.md) | The SetPresharedKeyForId_OUT structure holds the output data for the SetPresharedKeyForId method. |
| [SetRADIUSSharedSecret_IN structure](ns-iscsiop--setradiussharedsecret-in.md) | The SetRADIUSSharedSecret_IN structure holds the input data for the SetRADIUSSharedSecret method. |
| [SetRADIUSSharedSecret_OUT structure](ns-iscsiop--setradiussharedsecret-out.md) | The SetRADIUSSharedSecret_OUT structure holds the output data for the SetRADIUSSharedSecret method. |
| [SetTunnelModeOuterAddress_IN structure](ns-iscsiop--settunnelmodeouteraddress-in.md) | The SetTunnelModeOuterAddress_IN structure holds the input data for the SetTunnelModeOuterAddress method. |
| [SetTunnelModeOuterAddress_OUT structure](ns-iscsiop--settunnelmodeouteraddress-out.md) | The SetTunnelModeOuterAddress_OUT structure holds the output data for the SetTunnelModeOuterAddress method. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [PISCSI_ADAPTER_EVENT_CODE enumeration](ne-iscsiop-piscsi-adapter-event-code.md) | The ISCSI_ADAPTER_EVENT_CODE enumeration indicates the type of adapter event. |
| [PLOGINSESSIONTYPE enumeration](ne-iscsiop-ploginsessiontype.md) | The LOGINSESSIONTYPE enumeration indicates the type of logon session. |
