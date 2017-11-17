# Declarations in the ndis header
This header Ndis contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [NdisDestroyLookaheadBufferFromSharedMemory function](nf-ndis-ndisdestroylookaheadbufferfromsharedmemory.md) | TBD |
| [NdisMCmRegisterAddressFamilyEx function](nf-ndis-ndismcmregisteraddressfamilyex.md) | The NdisMCmRegisterAddressFamilyEx function registers an address family (AF) for communication between a miniport call manager (MCM) and CoNDIS clients. |
| [NdisSetTimerEx function](nf-ndis-ndissettimerex.md) | TBD |
| [NdisInitAnsiString function](nf-ndis-ndisinitansistring.md) | The NdisInitAnsiString function initializes a counted ANSI string. |
| [NdisCopyFromPacketToPacketSafe function](nf-ndis-ndiscopyfrompackettopacketsafe.md) | TBD |
| [NDIS_OOB_DATA_FROM_PACKET function](nf-ndis-ndis-oob-data-from-packet.md) | TBD |
| [NdisOpenConfigurationEx function](nf-ndis-ndisopenconfigurationex.md) | NDIS drivers call the NdisOpenConfigurationEx function to get a configuration handle that allows access to configuration parameters in the registry. |
| [NdisFreeSpinLock function](nf-ndis-ndisfreespinlock.md) | The NdisFreeSpinLock function releases a spin lock initialized in a preceding call to the NdisAllocateSpinLock functioin. |
| [NDIS_PACKET_FIRST_NDIS_BUFFER function](nf-ndis-ndis-packet-first-ndis-buffer.md) | TBD |
| [MINIPORT_SYNCHRONOUS_OID_REQUEST function](nf-ndis-miniport-synchronous-oid-request.md) | TBD |
| [NDIS_DECLARE_MINIPORT_ADDDEVICE_CONTEXT function](nf-ndis-ndis-declare-miniport-adddevice-context.md) | TBD |
| [NdisSetPacketStatus function](nf-ndis-ndissetpacketstatus.md) | TBD |
| [NdisDprReleaseSpinLock function](nf-ndis-ndisdprreleasespinlock.md) | The NdisDprReleaseSpinLock function releases a spin lock acquired in the immediately preceding call to the NdisDprAcquireSpinLock function. |
| [NDIS_DECLARE_CONTEXT_INNER function](nf-ndis-ndis-declare-context-inner.md) | TBD |
| [NdisOpenConfigurationKeyByIndex function](nf-ndis-ndisopenconfigurationkeybyindex.md) | The NdisOpenConfigurationKeyByIndex function opens a subkey of a given open registry key that is designated by a caller-supplied handle. |
| [NET_BUFFER_FIRST_SHARED_MEM_INFO function](nf-ndis-net-buffer-first-shared-mem-info.md) | TBD |
| [NdisMapFile function](nf-ndis-ndismapfile.md) | The NdisMapFile function maps an already open file into a caller-accessible buffer if the file is currently unmapped. |
| [NdisFreeNetBufferListContext function](nf-ndis-ndisfreenetbufferlistcontext.md) | Call the NdisFreeNetBufferListContext function to release context space in the NET_BUFFER_LIST_CONTEXT structure of a NET_BUFFER_LIST structure. |
| [NdisFreeBuffer function](nf-ndis-ndisfreebuffer.md) | TBD |
| [NdisGetSharedDataAlignment function](nf-ndis-ndisgetshareddataalignment.md) | NdisGetSharedDataAlignment returns the preferred alignment for memory structures that can be shared by more than one processor. |
| [NdisFSynchronousOidRequest function](nf-ndis-ndisfsynchronousoidrequest.md) | This function is reserved. |
| [NdisSetTimer function](nf-ndis-ndissettimer.md) | TBD |
| [NDIS_SET_PACKET_MEDIA_SPECIFIC_INFO function](nf-ndis-ndis-set-packet-media-specific-info.md) | TBD |
| [DECLARE_NDIS_HANDLE function](nf-ndis-declare-ndis-handle.md) | TBD |
| [NdisRegisterProtocol function](nf-ndis-ndisregisterprotocol.md) | TBD |
| [NdisCoSendNetBufferLists function](nf-ndis-ndiscosendnetbufferlists.md) | The NdisCoSendNetBufferLists function sends network data that is contained in a specified list of NET_BUFFER_LIST structures. |
| [NET_BUFFER_SHARED_MEM_OFFSET function](nf-ndis-net-buffer-shared-mem-offset.md) | TBD |
| [NdisCmDispatchIncomingCloseCall function](nf-ndis-ndiscmdispatchincomingclosecall.md) | NdisCmDispatchIncomingCloseCall tells a client to tear down an active or offered call, usually because the call manager has received a request from the network to close the connection. |
| [NdisMCmActivateVc function](nf-ndis-ndismcmactivatevc.md) | NdisMCmActivateVc notifies NDIS that an MCM driver is ready to make transfers on a particular VC. |
| [NdisCloseConfiguration function](nf-ndis-ndiscloseconfiguration.md) | The NdisCloseConfiguration function releases the handle to the registry key that was returned by the NdisOpenConfigurationEx, NdisOpenConfigurationKeyByIndex, or NdisOpenConfigurationKeyByName function. |
| [NdisReturnPackets function](nf-ndis-ndisreturnpackets.md) | TBD |
| [NdisMSetAttributes function](nf-ndis-ndismsetattributes.md) | TBD |
| [NdisBufferLength function](nf-ndis-ndisbufferlength.md) | TBD |
| [NdisUnchainBufferAtFront function](nf-ndis-ndisunchainbufferatfront.md) | TBD |
| [NdisMNetPnPEvent function](nf-ndis-ndismnetpnpevent.md) | NDIS miniport drivers (and intermediate drivers that are registered as miniport drivers) call the NdisMNetPnPEvent function to originate a network Plug and Play event, an NDIS PnP event, or Power Management event or propagate it to overlying drivers. |
| [NdisPrintString function](nf-ndis-ndisprintstring.md) | TBD |
| [NdisMQueryAdapterResources function](nf-ndis-ndismqueryadapterresources.md) | TBD |
| [NdisFreeFragmentNetBufferList function](nf-ndis-ndisfreefragmentnetbufferlist.md) | Call the NdisFreeFragmentNetBufferList function to free a NET_BUFFER_LIST structure and all associated NET_BUFFER structures and MDL chains that were previously allocated by the calling NdisAllocateFragmentNetBufferList function. |
| [NET_BUFFER_LIST_SET_HASH_TYPE function](nf-ndis-net-buffer-list-set-hash-type.md) | TBD |
| [NdisFIndicateStatus function](nf-ndis-ndisfindicatestatus.md) | The NdisFIndicateStatus function passes on a filtered status indication from an underlying driver or originates a status indication. |
| [NdisAllocatePacketPool function](nf-ndis-ndisallocatepacketpool.md) | TBD |
| [NET_BUFFER_SHARED_MEM_LENGTH function](nf-ndis-net-buffer-shared-mem-length.md) | TBD |
| [NdisCancelDirectOidRequest function](nf-ndis-ndiscanceldirectoidrequest.md) | Protocol drivers call the NdisCancelDirectOidRequest function to cancel a previous direct OID request to the underlying drivers. |
| [NdisMFlushLog function](nf-ndis-ndismflushlog.md) | NdisMFlushLog clears the log file. |
| [NdisCmDeactivateVc function](nf-ndis-ndiscmdeactivatevc.md) | NdisCmDeactivateVc notifies NDIS and the underlying miniport driver that there will be no further transfers on a particular active VC. |
| [NdisIfDeleteIfStackEntry function](nf-ndis-ndisifdeleteifstackentry.md) | The NdisIfDeleteIfStackEntry function deletes information about the ordering of two network interfaces in the NDIS interface stack. |
| [NdisSynchronousOidRequest function](nf-ndis-ndissynchronousoidrequest.md) | Protocol drivers call the NdisSynchronousOidRequest function to originate a new Synchronous OID request and issue it to underlying drivers. |
| [NdisGetRssProcessorInformation function](nf-ndis-ndisgetrssprocessorinformation.md) | The NdisGetRssProcessorInformation function retrieves information about the set of processors that a miniport driver must use for receive side scaling (RSS). |
| [NdisFreeToNPagedLookasideList function](nf-ndis-ndisfreetonpagedlookasidelist.md) | The NdisFreeToNPagedLookasideList function returns an entry to the given lookaside list. |
| [NdisReleaseRWLock function](nf-ndis-ndisreleaserwlock.md) | The NdisReleaseRWLock function releases a read/write lock that the caller uses to gain access to resources that are shared between driver threads. |
| [NdisSend function](nf-ndis-ndissend.md) | TBD |
| [NdisMaxGroupCount function](nf-ndis-ndismaxgroupcount.md) | The NdisMaxGroupCount function returns the maximum number of processor groups in the local computer system. |
| [NET_BUFFER_LIST_GET_HASH_TYPE function](nf-ndis-net-buffer-list-get-hash-type.md) | TBD |
| [NET_BUFFER_DATA_PHYSICAL_ADDRESS function](nf-ndis-net-buffer-data-physical-address.md) | TBD |
| [NdisCurrentGroupAndProcessor function](nf-ndis-ndiscurrentgroupandprocessor.md) | The NdisCurrentGroupAndProcessor function returns the group-relative processor number and group number of the current processor. |
| [NdisRawReadPortBufferUshort function](nf-ndis-ndisrawreadportbufferushort.md) | NdisRawReadPortBufferUshort reads a specified number of USHORTs into a caller-supplied buffer. |
| [NdisMIdleNotificationComplete function](nf-ndis-ndismidlenotificationcomplete.md) | Miniport drivers call NdisMIdleNotificationComplete to complete a pending idle notification for an NDIS selective suspend operation. NDIS begins the operation when it calls the driver's MiniportIdleNotification handler function. |
| [NdisMIndicateStatusEx function](nf-ndis-ndismindicatestatusex.md) | The NdisMIndicateStatusEx function reports a change in the status of a miniport adapter. |
| [NDIS_GET_PACKET_TIME_SENT function](nf-ndis-ndis-get-packet-time-sent.md) | TBD |
| [FILTER_SYNCHRONOUS_OID_REQUEST function](nf-ndis-filter-synchronous-oid-request.md) | TBD |
| [NdisFreeMdl function](nf-ndis-ndisfreemdl.md) | The NdisFreeMdl function frees an MDL that was allocated by calling the NdisAllocateMdl function. |
| [NdisFreeMemoryWithTagPriority function](nf-ndis-ndisfreememorywithtagpriority.md) | The NdisFreeMemoryWithTagPriority function releases memory that was allocated with the NdisAllocateMemoryWithTagPriority function. |
| [NET_BUFFER_NEXT_NB function](nf-ndis-net-buffer-next-nb.md) | TBD |
| [NdisInitializeString function](nf-ndis-ndisinitializestring.md) | The NdisInitializeString function allocates storage for and initializes a counted string in the system-default character set. |
| [NdisInitializeWorkItem function](nf-ndis-ndisinitializeworkitem.md) | TBD |
| [NdisFreeCloneNetBufferList function](nf-ndis-ndisfreeclonenetbufferlist.md) | Call the NdisFreeCloneNetBufferList function to free a NET_BUFFER_LIST structure and all associated NET_BUFFER structures and MDL chains that were previously allocated by calling the NdisAllocateCloneNetBufferList function. |
| [NdisAllocatePacket function](nf-ndis-ndisallocatepacket.md) | TBD |
| [NdisRawWritePortUlong function](nf-ndis-ndisrawwriteportulong.md) | NdisRawWritePortUlong writes a ULONG value to an I/O port on the NIC. |
| [NET_BUFFER_LIST_STATUS function](nf-ndis-net-buffer-list-status.md) | TBD |
| [NdisAllocateSharedMemory function](nf-ndis-ndisallocatesharedmemory.md) | The NdisAllocateSharedMemory function allocates shared memory from a shared memory provider. |
| [NdisUpcaseUnicodeString function](nf-ndis-ndisupcaseunicodestring.md) | The NdisUpcaseUnicodeString function converts a copy of a given Unicode string to upper case and returns the converted string.Note  This function is deprecated for NDIS 6.0 and later. |
| [NdisGetCurrentSystemTime function](nf-ndis-ndisgetcurrentsystemtime.md) | The NdisGetCurrentSystemTime function returns the current system time, suitable for setting timestamps. |
| [NDIS_GET_PACKET_TIME_RECEIVED function](nf-ndis-ndis-get-packet-time-received.md) | TBD |
| [NdisGroupMaxProcessorCount function](nf-ndis-ndisgroupmaxprocessorcount.md) | The NdisGroupMaxProcessorCount function determines the maximum number of processors in a specified processor group. |
| [NdisRetrieveUlong function](nf-ndis-ndisretrieveulong.md) | The NdisRetrieveUlong function retrieves a ULONG value from the source address, avoiding alignment faults. |
| [NdisInterlockedInsertHeadList function](nf-ndis-ndisinterlockedinsertheadlist.md) | The NdisInterlockedInsertHeadList function inserts an entry, usually a packet, at the head of a doubly linked list so that access to the list is synchronized in a multiprocessor-safe way. |
| [NdisOpenAdapterEx function](nf-ndis-ndisopenadapterex.md) | A protocol driver calls the NdisOpenAdapterEx function from its ProtocolBindAdapterEx function to set up a binding between the protocol driver and an underlying driver. |
| [NdisAllocateNetBufferAndNetBufferList function](nf-ndis-ndisallocatenetbufferandnetbufferlist.md) | Call the NdisAllocateNetBufferAndNetBufferList function to allocate and initialize a NET_BUFFER_LIST structure that is initialized with a preallocated NET_BUFFER structure. |
| [NdisCloseAdapter function](nf-ndis-ndiscloseadapter.md) | TBD |
| [NdisCmRegisterSapComplete function](nf-ndis-ndiscmregistersapcomplete.md) | NdisCmRegisterSapComplete returns the final status of a client's request, for which the CM previously returned NDIS_STATUS_PENDING, to register a SAP. |
| [NdisEnumerateFilterModules function](nf-ndis-ndisenumeratefiltermodules.md) | The NdisEnumerateFilterModules function enumerates all the filters modules and filter intermediate driver instances in a filter stack. |
| [NdisMEthIndicateReceiveComplete function](nf-ndis-ndismethindicatereceivecomplete.md) | TBD |
| [NdisMCmOpenAddressFamilyComplete function](nf-ndis-ndismcmopenaddressfamilycomplete.md) | NdisMCmOpenAddressFamilyComplete returns the final status of a client's request, for which the MCM driver's ProtocolCmOpenAf function returned NDIS_STATUS_PENDING, to open the MCM driver's address family. |
| [NdisQueryPacketLength function](nf-ndis-ndisquerypacketlength.md) | TBD |
| [NdisAllocateBufferPool function](nf-ndis-ndisallocatebufferpool.md) | TBD |
| [NdisMAllocatePort function](nf-ndis-ndismallocateport.md) | The NdisMAllocatePort function allocates an NDIS port that is associated with a miniport adapter. |
| [NdisIfDeregisterInterface function](nf-ndis-ndisifderegisterinterface.md) | The NdisIfDeregisterInterface function deregisters an NDIS network interface that was previously registered by a call to the NdisIfRegisterInterface function. |
| [NdisOpenConfigurationKeyByName function](nf-ndis-ndisopenconfigurationkeybyname.md) | The NdisOpenConfigurationKeyByName function opens a named subkey of a given open registry key that is designated by a caller-supplied handle. |
| [NDIS_SET_NET_BUFFER_LIST_CANCEL_ID function](nf-ndis-ndis-set-net-buffer-list-cancel-id.md) | TBD |
| [NdisFDeregisterFilterDriver function](nf-ndis-ndisfderegisterfilterdriver.md) | A filter drivers calls the NdisFDeregisterFilterDriver function to release resources that it previously allocated with the NdisFRegisterFilterDriver function. |
| [NdisOpenConfiguration function](nf-ndis-ndisopenconfiguration.md) | TBD |
| [NdisCopyReceiveNetBufferListInfo function](nf-ndis-ndiscopyreceivenetbufferlistinfo.md) | Intermediate drivers call the NdisCopyReceiveNetBufferListInfo function to copy the NET_BUFFER_LIST information in a received NET_BUFFER_LIST structure. |
| [NdisWriteRegisterUlong function](nf-ndis-ndiswriteregisterulong.md) | NdisWriteRegisterUlong is called by the miniport driver to write a ULONG to a memory-mapped device register. |
| [NDIS_DECLARE_CO_CM_VC_CONTEXT function](nf-ndis-ndis-declare-co-cm-vc-context.md) | TBD |
| [NDIS_RAISE_IRQL_TO_DISPATCH function](nf-ndis-ndis-raise-irql-to-dispatch.md) | TBD |
| [NBL_CLEAR_PROTOCOL_RSVD_FLAG function](nf-ndis-nbl-clear-protocol-rsvd-flag.md) | TBD |
| [NDIS_TEST_SEND_FLAG function](nf-ndis-ndis-test-send-flag.md) | TBD |
| [NdisFOidRequest function](nf-ndis-ndisfoidrequest.md) | Filter drivers call the NdisFOidRequest function to forward an OID request to underlying drivers or to originate such a request. |
| [NDIS_DECLARE_PROTOCOL_DRIVER_CONTEXT function](nf-ndis-ndis-declare-protocol-driver-context.md) | TBD |
| [NdisIMInitializeDeviceInstance function](nf-ndis-ndisiminitializedeviceinstance.md) | TBD |
| [NdisFDevicePnPEventNotify function](nf-ndis-ndisfdevicepnpeventnotify.md) | A filter driver can call the NdisFDevicePnPEventNotify function to forward a device Plug and Play (PnP) or Power Management event to underlying drivers. |
| [NdisReadNetworkAddress function](nf-ndis-ndisreadnetworkaddress.md) | The NdisReadNetworkAddress function returns the software-configurable network address that was stored in the registry for a NIC when it was installed in the machine. |
| [NdisMCmDispatchIncomingCallQoSChange function](nf-ndis-ndismcmdispatchincomingcallqoschange.md) | NdisMCmDispatchIncomingCallQoSChange notifies a client that a request to change the quality of service on that client's active connection has been received over the network. |
| [NdisPacketPoolUsage function](nf-ndis-ndispacketpoolusage.md) | TBD |
| [NdisCmRegisterAddressFamily function](nf-ndis-ndiscmregisteraddressfamily.md) | TBD |
| [NdisMInitializeScatterGatherDma function](nf-ndis-ndisminitializescattergatherdma.md) | TBD |
| [NdisInitializeEvent function](nf-ndis-ndisinitializeevent.md) | The NdisInitializeEvent function sets up an event object during driver initialization to be used subsequently as a synchronization mechanism. |
| [NdisMFreeNetBufferSGList function](nf-ndis-ndismfreenetbuffersglist.md) | Bus-master miniport drivers call the NdisMFreeNetBufferSGList function to free scatter/gather list resources that were allocated by calling the NdisMAllocateNetBufferSGList function. |
| [NET_BUFFER_LIST_PROTOCOL_RESERVED function](nf-ndis-net-buffer-list-protocol-reserved.md) | TBD |
| [NDIS_DECLARE_FILTER_MODULE_CONTEXT function](nf-ndis-ndis-declare-filter-module-context.md) | TBD |
| [NdisCopyFromNetBufferToNetBuffer function](nf-ndis-ndiscopyfromnetbuffertonetbuffer.md) | Call the NdisCopyFromNetBufferToNetBuffer function to copy data from a source NET_BUFFER structure to a destination NET_BUFFER structure. |
| [NdisMoveMappedMemory function](nf-ndis-ndismovemappedmemory~r1.md) | TBD |
| [NdisGetCurrentProcessorCpuUsage function](nf-ndis-ndisgetcurrentprocessorcpuusage.md) | The NdisGetCurrentProcessorCpuUsage function returns the average amount of activity on the current processor since boot as a percentage.Note  This function is deprecated. |
| [NET_BUFFER_LIST_SET_HASH_FUNCTION function](nf-ndis-net-buffer-list-set-hash-function.md) | TBD |
| [NdisGetNextBuffer function](nf-ndis-ndisgetnextbuffer.md) | TBD |
| [NdisInitializeSListHead function](nf-ndis-ndisinitializeslisthead.md) | The NdisInitializeSListHead function initializes the head of a sequenced, interlocked, singly linked list. |
| [NdisMSetInformationComplete function](nf-ndis-ndismsetinformationcomplete.md) | TBD |
| [NdisMWanSendComplete function](nf-ndis-ndismwansendcomplete.md) | TBD |
| [NdisGetPoolFromNetBuffer function](nf-ndis-ndisgetpoolfromnetbuffer.md) | Call the NdisGetPoolFromNetBuffer function to get the NET_BUFFER structure pool handle that is associated with a specified NET_BUFFER structure. |
| [NET_BUFFER_LIST_INFO function](nf-ndis-net-buffer-list-info.md) | TBD |
| [NDIS_PACKET_EXTENSION_FROM_PACKET function](nf-ndis-ndis-packet-extension-from-packet.md) | TBD |
| [NdisMTransferDataComplete function](nf-ndis-ndismtransferdatacomplete.md) | TBD |
| [NdisMCmDeactivateVc function](nf-ndis-ndismcmdeactivatevc.md) | NdisMCmDeactivateVc notifies NDIS that there will be no further transfers on a particular active VC. |
| [NdisMTriggerPDDrainNotification function](nf-ndis-ndismtriggerpddrainnotification.md) | TBD |
| [NdisIfAddIfStackEntry function](nf-ndis-ndisifaddifstackentry.md) | The NdisIfAddIfStackEntry function specifies the ordering of two network interfaces in the NDIS network interface stack. |
| [NdisClOpenAddressFamily function](nf-ndis-ndisclopenaddressfamily.md) | TBD |
| [NdisMAllocateSharedMemoryAsync function](nf-ndis-ndismallocatesharedmemoryasync.md) | TBD |
| [NdisMDeregisterIoPortRange function](nf-ndis-ndismderegisterioportrange.md) | NdisMDeregisterIoPortRange releases a mapping that was set up with NdisMRegisterIoPortRange during driver initialization. |
| [NdisAllocateNetBufferMdlAndData function](nf-ndis-ndisallocatenetbuffermdlanddata.md) | NDIS drivers call the NdisAllocateNetBufferMdlAndData function to allocate a NET_BUFFER structure along with the associated MDL and data. |
| [NdisCopyFromPacketToPacket function](nf-ndis-ndiscopyfrompackettopacket.md) | TBD |
| [NdisCancelSendNetBufferLists function](nf-ndis-ndiscancelsendnetbufferlists.md) | Protocol drivers call the NdisCancelSendNetBufferLists function to cancel the transmission of network data. |
| [NDIS_DECLARE_CO_MINIPORT_VC_CONTEXT function](nf-ndis-ndis-declare-co-miniport-vc-context.md) | TBD |
| [NDIS_INIT_FUNCTION function](nf-ndis-ndis-init-function.md) | TBD |
| [NdisAdjustMdlLength function](nf-ndis-ndisadjustmdllength.md) | The NdisAdjustMdlLength function modifies the length of the data that is associated with an MDL. |
| [NdisMCmCreateVc function](nf-ndis-ndismcmcreatevc.md) | NdisMCmCreateVc sets up a connection endpoint on which an MCM driver can dispatch an incoming-call offer to a client. |
| [NdisQueryDepthSList function](nf-ndis-ndisquerydepthslist.md) | The NdisQueryDepthSList function returns the current number of entries in a given sequenced, singly linked list. |
| [NBL_SET_PROT_RSVD_FLAG function](nf-ndis-nbl-set-prot-rsvd-flag.md) | TBD |
| [NDIS_NBL_GET_MEDIA_SPECIFIC_INFO_EX function](nf-ndis-ndis-nbl-get-media-specific-info-ex.md) | TBD |
| [NdisQueryBufferSafe function](nf-ndis-ndisquerybuffersafe.md) | TBD |
| [NdisMDirectOidRequestComplete function](nf-ndis-ndismdirectoidrequestcomplete.md) | Miniport drivers call the NdisMDirectOidRequestComplete function to return the final status of a direct OID request for which the driver's MiniportDirectOidRequest function returned NDIS_STATUS_PENDING. |
| [NdisDeleteNPagedLookasideList function](nf-ndis-ndisdeletenpagedlookasidelist.md) | The NdisDeleteNPagedLookasideList function removes a nonpaged lookaside list from the system. |
| [NdisMoveMappedMemory function](nf-ndis-ndismovemappedmemory.md) | TBD |
| [NdisMIndicateStatus function](nf-ndis-ndismindicatestatus.md) | TBD |
| [NdisInitializeNPagedLookasideList function](nf-ndis-ndisinitializenpagedlookasidelist.md) | The NdisInitializeNPagedLookasideList function initializes a lookaside list. After a successful initialization, nonpaged fixed-size blocks can be allocated from and freed to the lookaside list. |
| [NDIS_DECLARE_SWITCH_NET_BUFFER_LIST_CONTEXT_TYPE function](nf-ndis-ndis-declare-switch-net-buffer-list-context-type.md) | TBD |
| [NDIS_PAGABLE_FUNCTION function](nf-ndis-ndis-pagable-function.md) | TBD |
| [NdisCmCloseCallComplete function](nf-ndis-ndiscmclosecallcomplete.md) | NdisCmCloseCallComplete returns the final status of a client's request, for which the call manager previously returned NDIS_STATUS_PENDING, to tear down a call. |
| [NdisAllocateMemoryWithTag function](nf-ndis-ndisallocatememorywithtag.md) | TBD |
| [NdisFReturnNetBufferLists function](nf-ndis-ndisfreturnnetbufferlists.md) | Filter drivers call NdisFReturnNetBufferLists to release the ownership of one or more NET_BUFFER_LIST structures and their associated NET_BUFFER structures. |
| [NdisFIndicateReceiveNetBufferLists function](nf-ndis-ndisfindicatereceivenetbufferlists.md) | A filter driver calls NdisFIndicateReceiveNetBufferLists to indicate that it has received network data. For more information, see Receiving Data in a Filter Driver. |
| [NDIS_DECLARE_MINIPORT_DRIVER_CONTEXT function](nf-ndis-ndis-declare-miniport-driver-context.md) | TBD |
| [NET_BUFFER_LIST_RECEIVE_FILTER_VPORT_ID function](nf-ndis-net-buffer-list-receive-filter-vport-id.md) | TBD |
| [NdisReadRegisterUshort function](nf-ndis-ndisreadregisterushort.md) | NdisReadRegisterUshort is called by the miniport driver to read a USHORT from a memory-mapped device register. |
| [NDIS_GET_NET_BUFFER_LIST_VIRTUAL_SUBNET_ID function](nf-ndis-ndis-get-net-buffer-list-virtual-subnet-id.md) | TBD |
| [NdisDprAllocatePacketNonInterlocked function](nf-ndis-ndisdprallocatepacketnoninterlocked.md) | TBD |
| [NdisMSetBusData function](nf-ndis-ndismsetbusdata.md) | NDIS drivers call the NdisMSetBusData function to write to the configuration space of a device. |
| [NdisMCoIndicateStatusEx function](nf-ndis-ndismcoindicatestatusex.md) | The NdisMCoIndicateStatusEx function reports a change in the status of a CoNDIS miniport adapter. |
| [NdisFGetOptionalSwitchHandlers function](nf-ndis-ndisfgetoptionalswitchhandlers.md) | Hyper-V extensible switch extensions call the NdisFGetOptionalSwitchHandlers function to obtain a list of pointers to the Hyper-V extensible switch handler functions. |
| [NdisMIdleNotificationConfirm function](nf-ndis-ndismidlenotificationconfirm.md) | Miniport drivers call NdisMIdleNotificationConfirm to notify NDIS that the idle network adapter can safely be suspended and transitioned to a low-power state.Miniport drivers call this function during an NDIS selective suspend operation. |
| [NdisDprAllocatePacket function](nf-ndis-ndisdprallocatepacket.md) | TBD |
| [NdisIMGetBindingContext function](nf-ndis-ndisimgetbindingcontext.md) | The NdisIMGetBindingContext function allows an NDIS protocol driver to access the device context area, which was created by an underlying intermediate driver, for a virtual miniport to which the higher level protocol driver is bound. |
| [NdisCmOpenAddressFamilyComplete function](nf-ndis-ndiscmopenaddressfamilycomplete.md) | NdisCmOpenAddressFamilyComplete returns the final status of a stand-alone call manager's open of a given AF for a particular client after the call manager returned NDIS_STATUS_PENDING in response to that client's original open-AF request. |
| [NdisGetPacketFlags function](nf-ndis-ndisgetpacketflags.md) | TBD |
| [NdisReset function](nf-ndis-ndisreset.md) | TBD |
| [NDIS_BUFFER_TO_SPAN_PAGES function](nf-ndis-ndis-buffer-to-span-pages.md) | TBD |
| [NdisMCmRegisterAddressFamily function](nf-ndis-ndismcmregisteraddressfamily.md) | TBD |
| [NdisCopyLookaheadData function](nf-ndis-ndiscopylookaheaddata.md) | TBD |
| [NdisGetBufferPhysicalArraySize function](nf-ndis-ndisgetbufferphysicalarraysize.md) | TBD |
| [NdisGroupActiveProcessorCount function](nf-ndis-ndisgroupactiveprocessorcount.md) | The NdisGroupActiveProcessorCount function returns the number of processors that are currently active in a specified group. |
| [NdisFRestartFilter function](nf-ndis-ndisfrestartfilter.md) | A filter driver calls the NdisFRestartFilter function to request NDIS to initiate a restart operation for a filter module. |
| [NdisIfAllocateNetLuidIndex function](nf-ndis-ndisifallocatenetluidindex.md) | The NdisIfAllocateNetLuidIndex function allocates a NET_LUID index for an NDIS network interface provider. |
| [NDIS_GET_PACKET_TIME_TO_SEND function](nf-ndis-ndis-get-packet-time-to-send.md) | TBD |
| [NdisSendNetBufferLists function](nf-ndis-ndissendnetbufferlists.md) | Protocol drivers call the NdisSendNetBufferLists function to send network data that is contained in a list of NET_BUFFER_LIST structures. |
| [NdisAllocateFromNPagedLookasideList function](nf-ndis-ndisallocatefromnpagedlookasidelist.md) | The NdisAllocateFromNPagedLookasideList function removes the first entry from the given lookaside list head. If the lookaside list currently is empty, an entry is allocated from nonpaged pool. |
| [NdisMCoIndicateReceiveNetBufferLists function](nf-ndis-ndismcoindicatereceivenetbufferlists.md) | The NdisMCoIndicateReceiveNetBufferLists function indicates that the miniport driver received data from the network. |
| [NBL_TEST_FLAG function](nf-ndis-nbl-test-flag.md) | TBD |
| [NdisFCancelSendNetBufferLists function](nf-ndis-ndisfcancelsendnetbufferlists.md) | Filter drivers call the NdisFCancelSendNetBufferLists function to cancel the transmission of network data. |
| [NdisMSynchronizeWithInterrupt function](nf-ndis-ndismsynchronizewithinterrupt.md) | TBD |
| [NdisMSetMiniportAttributes function](nf-ndis-ndismsetminiportattributes.md) | A miniport driver must call the NdisMSetMiniportAttributes function from its MiniportInitializeEx function to identify a context area for miniport adapter to NDIS, and to provide NDIS with information about the miniport adapter. |
| [NdisMQueryAdapterInstanceName function](nf-ndis-ndismqueryadapterinstancename.md) | The NdisMQueryAdapterInstanceName function retrieves the friendly name of a miniport adapter. |
| [NdisMGetDmaAlignment function](nf-ndis-ndismgetdmaalignment.md) | The NdisMGetDmaAlignment function returns the alignment requirements of the DMA system for a NIC. |
| [NET_BUFFER_LIST_GFT_OFFLOAD_INFO function](nf-ndis-net-buffer-list-gft-offload-info.md) | TBD |
| [NDIS_PACKET_VALID_COUNTS function](nf-ndis-ndis-packet-valid-counts.md) | TBD |
| [NdisIMNotifyPnPEvent function](nf-ndis-ndisimnotifypnpevent.md) | TBD |
| [NdisGetNetBufferListProtocolId function](nf-ndis-ndisgetnetbufferlistprotocolid.md) | The NdisGetNetBufferListProtocolId function retrieves the protocol identifier from the NetBufferListInfo member of a NET_BUFFER_LIST structure. |
| [NdisClCloseAddressFamily function](nf-ndis-ndisclcloseaddressfamily.md) | NdisClCloseAddressFamily releases the association between a client protocol and a call manager's or MCM driver's registered AF for a particular NIC to which the client is bound. |
| [NdisProcessorIndexToNumber function](nf-ndis-ndisprocessorindextonumber.md) | TBD |
| [NdisCmDispatchCallConnected function](nf-ndis-ndiscmdispatchcallconnected.md) | NdisCmDispatchCallConnected notifies NDIS and the client that data transfers can begin on a VC that the call manager created for an incoming call initiated on a remote node. |
| [NdisRecalculatePacketCounts function](nf-ndis-ndisrecalculatepacketcounts.md) | TBD |
| [NdisOpenAdapter function](nf-ndis-ndisopenadapter.md) | TBD |
| [NdisClearNblFlag function](nf-ndis-ndisclearnblflag.md) | TBD |
| [NdisUpdateSharedMemory function](nf-ndis-ndisupdatesharedmemory.md) | TBD |
| [NdisMSendResourcesAvailable function](nf-ndis-ndismsendresourcesavailable.md) | TBD |
| [NdisMResetMiniport function](nf-ndis-ndismresetminiport.md) | A miniport driver calls the NdisMResetMiniport function to trigger a later reset operation from NDIS. |
| [NdisUnbindAdapter function](nf-ndis-ndisunbindadapter.md) | Protocol drivers call the NdisUnbindAdapter function to request NDIS to close a binding to an underlying miniport adapter. |
| [NDIS_GET_ORIGINAL_PACKET function](nf-ndis-ndis-get-original-packet.md) | TBD |
| [NDIS_DECLARE_FILTER_DRIVER_CONTEXT function](nf-ndis-ndis-declare-filter-driver-context.md) | TBD |
| [NdisZeroMappedMemory function](nf-ndis-ndiszeromappedmemory~r1.md) | NdisZeroMappedMemory fills a block of memory that was mapped with a preceding call to NdisMMapIoSpace with zeros. |
| [NdisFDirectOidRequest function](nf-ndis-ndisfdirectoidrequest.md) | Filter drivers call the NdisFDirectOidRequest function to forward a direct OID request to underlying drivers or to originate such a request. |
| [NdisAcquireRWLockWrite function](nf-ndis-ndisacquirerwlockwrite.md) | The NdisAcquireRWLockWrite function obtains a write lock that the caller uses for write access to resources that are shared between driver threads. |
| [NdisMReadDmaCounter function](nf-ndis-ndismreaddmacounter.md) | The NdisMReadDmaCounter function returns the current value of the system DMA controller's counter. |
| [NDIS_NBL_REMOVE_MEDIA_SPECIFIC_INFO function](nf-ndis-ndis-nbl-remove-media-specific-info.md) | TBD |
| [NdisMCoActivateVcComplete function](nf-ndis-ndismcoactivatevccomplete.md) | NdisMCoActivateVcComplete notifies NDIS and the call manager that the miniport driver has finished processing a CM-initiated activate-VC request, for which the miniport driver previously returned NDIS_STATUS_PENDING. |
| [NdisMRegisterInterrupt function](nf-ndis-ndismregisterinterrupt.md) | TBD |
| [NdisMSetTimer function](nf-ndis-ndismsettimer.md) | TBD |
| [NdisMSynchronizeWithInterruptEx function](nf-ndis-ndismsynchronizewithinterruptex.md) | Miniport drivers call the NdisMSynchronizeWithInterruptEx function to synchronize the execution of a miniport driver-supplied function with the MiniportInterrupt function. |
| [NdisMResetComplete function](nf-ndis-ndismresetcomplete.md) | The NdisMResetComplete function returns the final status of a reset request for which the miniport driver previously returned NDIS_STATUS_PENDING. |
| [NdisSetOptionalHandlers function](nf-ndis-ndissetoptionalhandlers.md) | NDIS drivers can call the NdisSetOptionalHandlers function to set or change the entry points of driver functions. |
| [NdisRequest function](nf-ndis-ndisrequest.md) | TBD |
| [NdisFreeNetBufferListPool function](nf-ndis-ndisfreenetbufferlistpool.md) | Call the NdisFreeNetBufferListPool function to free a NET_BUFFER_LIST structure pool. |
| [NDIS_TEST_RECEIVE_AT_DISPATCH_LEVEL function](nf-ndis-ndis-test-receive-at-dispatch-level.md) | TBD |
| [NET_BUFFER_LIST_COALESCED_SEG_COUNT function](nf-ndis-net-buffer-list-coalesced-seg-count.md) | TBD |
| [NET_BUFFER_SHARED_MEM_NEXT_SEGMENT function](nf-ndis-net-buffer-shared-mem-next-segment.md) | TBD |
| [NDIS_LOWER_IRQL function](nf-ndis-ndis-lower-irql.md) | TBD |
| [NdisCoGetTapiCallId function](nf-ndis-ndiscogettapicallid.md) | NdisCoGetTapiCallId retrieves a string that TAPI applications can use to identify a particular NDIS virtual connection (VC). |
| [NdisIMRegisterLayeredMiniport function](nf-ndis-ndisimregisterlayeredminiport.md) | TBD |
| [NET_BUFFER_LIST_FIRST_NB function](nf-ndis-net-buffer-list-first-nb.md) | TBD |
| [NdisInterlockedPopEntrySList function](nf-ndis-ndisinterlockedpopentryslist.md) | The NdisInterlockedPopEntrySList function removes the first entry from a sequenced, singly linked list. |
| [NDIS_TEST_SEND_COMPLETE_FLAG function](nf-ndis-ndis-test-send-complete-flag.md) | TBD |
| [NdisMCmRequest function](nf-ndis-ndismcmrequest.md) | TBD |
| [NdisCloseFile function](nf-ndis-ndisclosefile.md) | The NdisCloseFile function releases a handle returned by the NdisOpenFile function and frees the memory allocated to hold the file contents when it was opened. |
| [NDIS_SET_RECEIVE_FLAG function](nf-ndis-ndis-set-receive-flag.md) | TBD |
| [NdisSetPhysicalAddressLow function](nf-ndis-ndissetphysicaladdresslow.md) | NdisSetPhysicalAddressLow sets the low-order part of a given physical address to a given value. |
| [NET_BUFFER_SHARED_MEM_FLAGS function](nf-ndis-net-buffer-shared-mem-flags.md) | TBD |
| [NdisCoSendPackets function](nf-ndis-ndiscosendpackets.md) | TBD |
| [NdisReEnumerateProtocolBindings function](nf-ndis-ndisreenumerateprotocolbindings.md) | The NdisReEnumerateProtocolBindings function causes NDIS to call a protocol driver's ProtocolBindAdapterEx function one time for each miniport adapter for which the driver is configured to bind but to which the driver is not currently bound. |
| [NdisAllocateNetBufferList function](nf-ndis-ndisallocatenetbufferlist.md) | Call the NdisAllocateNetBufferList function to allocate and initialize a NET_BUFFER_LIST structure from a NET_BUFFER_LIST structure pool. |
| [NdisProcessorNumberToIndex function](nf-ndis-ndisprocessornumbertoindex.md) | TBD |
| [NdisMMapIoSpace function](nf-ndis-ndismmapiospace.md) | NdisMMapIoSpace maps a given bus-relative &#0034;physical&#0034; range of device RAM or registers onto a system-space virtual range. |
| [NDIS_MDL_LINKAGE function](nf-ndis-ndis-mdl-linkage.md) | TBD |
| [NdisDirectOidRequest function](nf-ndis-ndisdirectoidrequest.md) | The NdisDirectOidRequest function forwards a direct OID request to the underlying drivers to query the capabilities or status of an adapter or set the state of an adapter. |
| [NdisIfRegisterInterface function](nf-ndis-ndisifregisterinterface.md) | The NdisIfRegisterInterface function registers an NDIS network interface. |
| [NdisQuerySendFlags function](nf-ndis-ndisquerysendflags.md) | TBD |
| [NdisFCancelOidRequest function](nf-ndis-ndisfcanceloidrequest.md) | Filter drivers call the NdisFCancelOidRequest function to cancel a previous request to the underlying drivers. |
| [NdisCmRegisterAddressFamilyEx function](nf-ndis-ndiscmregisteraddressfamilyex.md) | The NdisCmRegisterAddressFamilyEx function registers an address family (AF) for communication between CoNDIS drivers. |
| [NdisCurrentProcessorIndex function](nf-ndis-ndiscurrentprocessorindex.md) | The NdisCurrentProcessorIndex function returns the system-assigned number of the current processor that the caller is running on. |
| [NDIS_STATUS_INDICATION_TEST_FLAG function](nf-ndis-ndis-status-indication-test-flag.md) | TBD |
| [NdisMRegisterDevice function](nf-ndis-ndismregisterdevice.md) | TBD |
| [NdisQueueIoWorkItem function](nf-ndis-ndisqueueioworkitem.md) | NDIS drivers call the NdisQueueIoWorkItem function to queue a work item. |
| [NdisSetNblFlag function](nf-ndis-ndissetnblflag.md) | TBD |
| [NdisFSetAttributes function](nf-ndis-ndisfsetattributes.md) | A filter driver calls the NdisFSetAttributes function to specify a filter module context area. |
| [NdisSetPhysicalAddressHigh function](nf-ndis-ndissetphysicaladdresshigh.md) | NdisSetPhysicalAddressHigh sets the high-order part of a given physical address to a given value. |
| [NdisRawWritePortBufferUchar function](nf-ndis-ndisrawwriteportbufferuchar.md) | NdisRawWritePortBufferUchar writes a specified number of bytes from a caller-supplied buffer to a given I/O port. |
| [NdisClGetProtocolVcContextFromTapiCallId function](nf-ndis-ndisclgetprotocolvccontextfromtapicallid.md) | NdisClGetProtocolVcContextFromTapiCallId retrieves the client context for a virtual connection (VC) identified by a TAPI Call ID string. |
| [NdisCopySendNetBufferListInfo function](nf-ndis-ndiscopysendnetbufferlistinfo.md) | Intermediate drivers call the NdisCopySendNetBufferListInfo function to copy the NET_BUFFER_LIST information in a transmit NET_BUFFER_LIST structure. |
| [NdisSetTimerObject function](nf-ndis-ndissettimerobject.md) | The NdisSetTimerObject function sets a timer object to fire after a specified interval or periodically. |
| [NdisMInitializeWrapper function](nf-ndis-ndisminitializewrapper.md) | TBD |
| [NdisRetreatNetBufferListDataStart function](nf-ndis-ndisretreatnetbufferlistdatastart.md) | Call the NdisRetreatNetBufferListDataStart function to increase the used data space in all the NET_BUFFER structures in a NET_BUFFER_LIST structure. |
| [NDIS_GET_NET_BUFFER_LIST_GFT_OFFLOAD_FLAGS function](nf-ndis-ndis-get-net-buffer-list-gft-offload-flags.md) | TBD |
| [NdisUnmapFile function](nf-ndis-ndisunmapfile.md) | The NdisUnmapFile function releases a virtual address mapping of a file previously set up with the NdisMapFile function. |
| [NdisClAddParty function](nf-ndis-ndiscladdparty.md) | NdisClAddParty adds a party on the client's multipoint VC. |
| [NdisCoOidRequestComplete function](nf-ndis-ndiscooidrequestcomplete.md) | The NdisCoOidRequestComplete function returns the final status of an OID request that a CoNDIS client's or stand-alone call manager's ProtocolCoOidRequest function previously returned NDIS_STATUS_PENDING for. |
| [NDIS_GET_PACKET_MEDIA_SPECIFIC_INFO function](nf-ndis-ndis-get-packet-media-specific-info.md) | TBD |
| [NdisGeneratePartialCancelId function](nf-ndis-ndisgeneratepartialcancelid.md) | The NdisGeneratePartialCancelId function returns a value that the calling driver must use as the high-order byte of a cancellation ID. |
| [NdisFreePacket function](nf-ndis-ndisfreepacket.md) | TBD |
| [NdisAllocateSpinLock function](nf-ndis-ndisallocatespinlock.md) | The NdisAllocateSpinLock function initializes a variable of type NDIS_SPIN_LOCK, used to synchronize access to resources shared among non-ISR driver functions. |
| [NdisMCoRequestComplete function](nf-ndis-ndismcorequestcomplete.md) | TBD |
| [NdisFreeMemoryWithTag function](nf-ndis-ndisfreememorywithtag.md) | The NdisFreeMemoryWithTag function is deprecated for all NDIS versions. Use NdisAllocateMemoryWithTagPriority instead. |
| [NdisZeroMemory function](nf-ndis-ndiszeromemory.md) | The NdisZeroMemory function fills a block of memory with zeros. |
| [NDIS_TEST_RETURN_FLAG function](nf-ndis-ndis-test-return-flag.md) | TBD |
| [NdisClearPacketFlags function](nf-ndis-ndisclearpacketflags.md) | TBD |
| [NdisChainBufferAtFront function](nf-ndis-ndischainbufferatfront.md) | TBD |
| [NdisMCoSendNetBufferListsComplete function](nf-ndis-ndismcosendnetbufferlistscomplete.md) | The NdisMCoSendNetBufferListsComplete function returns a linked list of NET_BUFFER_LIST structures to an overlying driver and returns the final status of a CoNDIS send request. |
| [NDIS_SET_NET_BUFFER_LIST_GFT_OFFLOAD_VPORT_ID function](nf-ndis-ndis-set-net-buffer-list-gft-offload-vport-id.md) | TBD |
| [NdisFRegisterFilterDriver function](nf-ndis-ndisfregisterfilterdriver.md) | A filter driver calls the NdisFRegisterFilterDriver function to register its FilterXxx functions with NDIS. |
| [NdisMCloseLog function](nf-ndis-ndismcloselog.md) | NdisMCloseLog releases resources that were used for logging. |
| [NdisMoveMemory function](nf-ndis-ndismovememory.md) | The NdisMoveMemory function copies a specified number of bytes from one caller-supplied location to another. |
| [NdisMIndicateStatusComplete function](nf-ndis-ndismindicatestatuscomplete.md) | TBD |
| [NdisSetPacketPoolProtocolId function](nf-ndis-ndissetpacketpoolprotocolid.md) | TBD |
| [NDIS_MAKE_RID function](nf-ndis-ndis-make-rid.md) | TBD |
| [NDIS_BUFFER_LINKAGE function](nf-ndis-ndis-buffer-linkage.md) | TBD |
| [NdisMGetVirtualFunctionBusData function](nf-ndis-ndismgetvirtualfunctionbusdata.md) | A miniport driver calls the NdisMGetVirtualFunctionBusData function to read data from the PCI Express (PCIe) configuration space of a specified Virtual Function (VF) on the network adapter. |
| [NDIS_NBL_ADD_MEDIA_SPECIFIC_INFO_EX function](nf-ndis-ndis-nbl-add-media-specific-info-ex.md) | TBD |
| [NdisMTrIndicateReceive function](nf-ndis-ndismtrindicatereceive.md) | TBD |
| [NdisAdjustNetBufferCurrentMdl function](nf-ndis-ndisadjustnetbuffercurrentmdl.md) | The NdisAdjustNetBufferCurrentMdl function updates a NET_BUFFER structure based on the current data offset. |
| [NDIS_SET_NET_BUFFER_LIST_VLAN_ID function](nf-ndis-ndis-set-net-buffer-list-vlan-id.md) | TBD |
| [NdisQueryMdl function](nf-ndis-ndisquerymdl.md) | TBD |
| [NdisGetVersion function](nf-ndis-ndisgetversion.md) | The NdisGetVersion function returns the version number of NDIS. |
| [NdisMGetVirtualDeviceLocation function](nf-ndis-ndismgetvirtualdevicelocation.md) | TBD |
| [AFFINITY_MASK function](nf-ndis-affinity-mask.md) | TBD |
| [NdisWritePcmciaAttributeMemory function](nf-ndis-ndiswritepcmciaattributememory.md) | TBD |
| [NdisMRegisterDmaChannel function](nf-ndis-ndismregisterdmachannel.md) | The NdisMRegisterDmaChannel function claims a system DMA controller channel during initialization for DMA operations on a subordinate NIC or on an ISA bus-master NIC. |
| [NBL_CLEAR_PROT_RSVD_FLAG function](nf-ndis-nbl-clear-prot-rsvd-flag.md) | TBD |
| [NdisCoDeleteVc function](nf-ndis-ndiscodeletevc.md) | NdisCoDeleteVc destroys a caller-created VC. |
| [NDIS_TEST_RECEIVE_CAN_PEND function](nf-ndis-ndis-test-receive-can-pend.md) | TBD |
| [NdisGetProcessorInformationEx function](nf-ndis-ndisgetprocessorinformationex.md) | The NdisGetProcessorInformationEx function retrieves information about the CPU topology of the local computer. |
| [NDIS_DECLARE_CO_CL_VC_CONTEXT function](nf-ndis-ndis-declare-co-cl-vc-context.md) | TBD |
| [NdisMoveToMappedMemory function](nf-ndis-ndismovetomappedmemory.md) | TBD |
| [NdisQueryNetBufferPhysicalCount function](nf-ndis-ndisquerynetbufferphysicalcount.md) | The NdisQueryNetBufferPhysicalCount function returns the maximum number of physical breaks mapped by the buffer descriptors that are associated with the given NET_BUFFER structure. |
| [NDIS_CLEAR_CLONE_FLAG function](nf-ndis-ndis-clear-clone-flag.md) | TBD |
| [NdisStallExecution function](nf-ndis-ndisstallexecution.md) | The NdisStallExecution function stalls the caller on the current processor for a given interval. |
| [NdisCmDropPartyComplete function](nf-ndis-ndiscmdroppartycomplete.md) | NdisCmDropPartyComplete returns the final status of a client's request, for which the call manager previously returned NDIS_STATUS_PENDING, to remove a party from a multipoint VC. |
| [NdisRawWritePortUchar function](nf-ndis-ndisrawwriteportuchar.md) | NdisRawWritePortUchar writes a byte to an I/O port on the NIC. |
| [NdisBuildScatterGatherList function](nf-ndis-ndisbuildscattergatherlist.md) | The NdisBuildScatterGatherList function builds a scatter/gather list by using the specified parameters. |
| [NdisMQueueDpc function](nf-ndis-ndismqueuedpc.md) | NDIS miniport drivers call the NdisMQueueDpc function to schedule DPC calls on CPUs. |
| [NDIS_GET_NET_BUFFER_LIST_VLAN_ID function](nf-ndis-ndis-get-net-buffer-list-vlan-id.md) | TBD |
| [DECLARE_NDIS_HANDLE function](nf-ndis-declare-ndis-handle~r1.md) | TBD |
| [NdisMCmDispatchIncomingDropParty function](nf-ndis-ndismcmdispatchincomingdropparty.md) | NdisMCmDispatchIncomingDropParty notifies a client that it should remove a particular party on a multipoint VC. |
| [NdisInterlockedPopEntryList function](nf-ndis-ndisinterlockedpopentrylist.md) | TBD |
| [NdisIfFreeNetLuidIndex function](nf-ndis-ndisiffreenetluidindex.md) | The NdisIfFreeNetLuidIndex function frees a network interface NET_LUID index that was previously allocated by a call to the NdisIfAllocateNetLuidIndex function. |
| [NdisMSendComplete function](nf-ndis-ndismsendcomplete.md) | TBD |
| [NET_BUFFER_DATA_LENGTH function](nf-ndis-net-buffer-data-length.md) | TBD |
| [NdisBufferVirtualAddressSafe function](nf-ndis-ndisbuffervirtualaddresssafe.md) | TBD |
| [NdisInterlockedFlushSList function](nf-ndis-ndisinterlockedflushslist.md) | TBD |
| [NdisQueryBuffer function](nf-ndis-ndisquerybuffer.md) | TBD |
| [NdisAllocateCloneOidRequest function](nf-ndis-ndisallocatecloneoidrequest.md) | The NdisAllocateCloneOidRequest function allocates memory for a new NDIS_OID_REQUEST structure and copies all the information from an existing NDIS_OID_REQUEST structure to the newly allocated structure. |
| [NdisMInitializeTimer function](nf-ndis-ndisminitializetimer.md) | TBD |
| [NdisCancelOidRequest function](nf-ndis-ndiscanceloidrequest.md) | Protocol drivers call the NdisCancelOidRequest function to cancel a previous request to the underlying drivers. |
| [NdisMCmDropPartyComplete function](nf-ndis-ndismcmdroppartycomplete.md) | NdisMCmDropPartyComplete returns the final status of a client's request, for which the MCM driver previously returned NDIS_STATUS_PENDING, to remove a party from a multipoint VC. |
| [NdisMFreeMapRegisters function](nf-ndis-ndismfreemapregisters.md) | TBD |
| [NdisMCmDeleteVc function](nf-ndis-ndismcmdeletevc.md) | NdisMCmDeleteVc destroys a caller-created VC. |
| [NdisMCmCloseAddressFamilyComplete function](nf-ndis-ndismcmcloseaddressfamilycomplete.md) | NdisMCmCloseAddressFamilyComplete returns the final status of a client's request, for which the MCM driver returned NDIS_STATUS_PENDING, to close the AF. |
| [NdisGetSystemUpTimeEx function](nf-ndis-ndisgetsystemuptimeex.md) | The NdisGetSystemUpTimeEx function returns the number of milliseconds that have elapsed since the computer was restarted. |
| [NdisCmDispatchIncomingCallQoSChange function](nf-ndis-ndiscmdispatchincomingcallqoschange.md) | NdisCmDispatchIncomingCallQoSChange notifies a client that a request to change the quality of service on that client's active connection has been received over the network. |
| [NdisMRegisterAdapterShutdownHandler function](nf-ndis-ndismregisteradaptershutdownhandler.md) | TBD |
| [NdisIMGetCurrentPacketStack function](nf-ndis-ndisimgetcurrentpacketstack.md) | TBD |
| [NdisAllocateFragmentNetBufferList function](nf-ndis-ndisallocatefragmentnetbufferlist.md) | Call the NdisAllocateFragmentNetBufferList function to create a new fragmented NET_BUFFER_LIST structure based upon the data in an existing NET_BUFFER_LIST structure. |
| [NdisCancelSendPackets function](nf-ndis-ndiscancelsendpackets.md) | TBD |
| [NdisSetEvent function](nf-ndis-ndissetevent.md) | The NdisSetEvent function sets a given event to the signaled state if it was not already Signaled. |
| [NdisRawReadPortUshort function](nf-ndis-ndisrawreadportushort.md) | NdisRawReadPortUshort reads a USHORT value from a given I/O port on the NIC. |
| [NdisReadPciSlotInformation function](nf-ndis-ndisreadpcislotinformation.md) | TBD |
| [NdisAllocateIoWorkItem function](nf-ndis-ndisallocateioworkitem.md) | NDIS drivers call the NdisAllocateIoWorkItem function to allocate a work item. For more information, see NDIS I/O Work Items. |
| [NdisCoCreateVc function](nf-ndis-ndiscocreatevc.md) | NdisCoCreateVc sets up a connection endpoint from which a client can make outgoing calls or on which a stand-alone call manager can dispatch incoming calls. |
| [NET_BUFFER_LIST_GFT_OFFLOAD_FLOW_ENTRY_ID function](nf-ndis-net-buffer-list-gft-offload-flow-entry-id.md) | TBD |
| [NdisWriteRegisterUchar function](nf-ndis-ndiswriteregisteruchar.md) | NdisWriteRegisterUchar is called by the miniport driver to write a UCHAR to a memory-mapped device register. |
| [NdisInterlockedDecrement function](nf-ndis-ndisinterlockeddecrement.md) | The NdisInterlockedDecrement function decrements a caller-supplied variable of type LONG as an atomic operation. |
| [NdisIMAssociateMiniport function](nf-ndis-ndisimassociateminiport.md) | The NdisIMAssociateMiniport function informs NDIS that the specified lower and upper interfaces for miniport and protocol drivers respectively belong to the same intermediate driver. |
| [NdisReadRegisterUchar function](nf-ndis-ndisreadregisteruchar.md) | NdisReadRegisterUchar is called by the miniport driver to read a UCHAR from a memory-mapped device register. |
| [NdisTestNblFlag function](nf-ndis-ndistestnblflag.md) | TBD |
| [NdisSetPacketFlags function](nf-ndis-ndissetpacketflags.md) | TBD |
| [NdisAllocateReassembledNetBufferList function](nf-ndis-ndisallocatereassemblednetbufferlist.md) | Call the NdisAllocateReassembledNetBufferList function to reassemble a fragmented NET_BUFFER_LIST structure. |
| [NdisTerminateWrapper function](nf-ndis-ndisterminatewrapper.md) | TBD |
| [NdisAllocateNetBuffer function](nf-ndis-ndisallocatenetbuffer.md) | Call the NdisAllocateNetBuffer function to allocate and initialize a NET_BUFFER structure from a NET_BUFFER structure pool. |
| [NdisGetFirstBufferFromPacketSafe function](nf-ndis-ndisgetfirstbufferfrompacketsafe.md) | TBD |
| [NDIS_API_VERSION_AVAILABLE function](nf-ndis-ndis-api-version-available.md) | TBD |
| [NdisMDeregisterAdapterShutdownHandler function](nf-ndis-ndismderegisteradaptershutdownhandler.md) | TBD |
| [NdisCompleteUnbindAdapterEx function](nf-ndis-ndiscompleteunbindadapterex.md) | A protocol driver calls the NdisCompleteUnbindAdapterEx function to complete an unbind operation for which the driver's ProtocolUnbindAdapterEx function returned NDIS_STATUS_PENDING. |
| [NdisAllocateBuffer function](nf-ndis-ndisallocatebuffer.md) | TBD |
| [NdisInitUnicodeString function](nf-ndis-ndisinitunicodestring.md) | The NdisInitUnicodeString function initializes a counted Unicode string. |
| [NdisMAllocateNetBufferSGList function](nf-ndis-ndismallocatenetbuffersglist.md) | Bus-master miniport drivers call the NdisMAllocateNetBufferSGList function to obtain a scatter/gather list for the network data that is associated with a NET_BUFFER structure. |
| [NDIS_DECLARE_MINIPORT_ADAPTER_CONTEXT function](nf-ndis-ndis-declare-miniport-adapter-context.md) | TBD |
| [NdisCmActivateVc function](nf-ndis-ndiscmactivatevc.md) | NdisCmActivateVc passes CM-supplied call parameters, including media parameters, for a particular VC down to the underlying miniport driver. |
| [NdisCmDeregisterSapComplete function](nf-ndis-ndiscmderegistersapcomplete.md) | NdisCmDeregisterSapComplete returns the final status of a client's request, for which the call manager previously returned NDIS_STATUS_PENDING, to deregister a SAP. |
| [NdisAllocateNetBufferPool function](nf-ndis-ndisallocatenetbufferpool.md) | Call the NdisAllocateNetBufferPool function to allocate a pool of NET_BUFFER structures. |
| [NdisFreeGenericObject function](nf-ndis-ndisfreegenericobject.md) | Call the NdisFreeGenericObject function to free a generic object that was created with the NdisAllocateGenericObject function. |
| [NdisMDeregisterMiniportDriver function](nf-ndis-ndismderegisterminiportdriver.md) | A miniport driver calls the NdisMDeregisterMiniportDriver function to release resources that it allocated with a previous call to the NdisMRegisterMiniportDriver function. |
| [NdisFreeNetBufferList function](nf-ndis-ndisfreenetbufferlist.md) | Call the NdisFreeNetBufferList function to free a NET_BUFFER_LIST structure that was previously allocated from a NET_BUFFER_LIST structure pool. |
| [NdisMSendNetBufferListsComplete function](nf-ndis-ndismsendnetbufferlistscomplete.md) | Miniport drivers call the NdisMSendNetBufferListsComplete function to return a linked list of NET_BUFFER_LIST structures to an overlying driver and to return the final status of a send request. |
| [NdisTestNblFlags function](nf-ndis-ndistestnblflags.md) | TBD |
| [NDIS_SET_NET_BUFFER_LIST_IM_RESERVED function](nf-ndis-ndis-set-net-buffer-list-im-reserved.md) | TBD |
| [NDIS_SWITCH_PORT_DESTINATION_AT_ARRAY_INDEX function](nf-ndis-ndis-switch-port-destination-at-array-index.md) | TBD |
| [NDIS_DECLARE_MINIPORT_SHARED_DMA_ASYNC_CONTEXT function](nf-ndis-ndis-declare-miniport-shared-dma-async-context.md) | TBD |
| [NdisAdvanceNetBufferDataStart function](nf-ndis-ndisadvancenetbufferdatastart.md) | Call the NdisAdvanceNetBufferDataStart function to release the used data space that was added with the NdisRetreatNetBufferDataStart function. |
| [NdisFNetPnPEvent function](nf-ndis-ndisfnetpnpevent.md) | A filter driver can call the NdisFNetPnPEvent function to forward a network Plug and Play (PnP) or Power Management event to overlying drivers. |
| [DECLARE_NDIS_HANDLE function](nf-ndis-declare-ndis-handle~r2.md) | TBD |
| [NdisMCoDeactivateVcComplete function](nf-ndis-ndismcodeactivatevccomplete.md) | NdisMCoDeactivateVcComplete notifies NDIS and the call manager that the miniport driver has finished processing a CM-initiated deactivate-VC request, for which the miniport driver previously returned NDIS_STATUS_PENDING. |
| [NdisRawReadPortBufferUlong function](nf-ndis-ndisrawreadportbufferulong.md) | NdisRawReadPortBufferUlong reads a specified number of ULONGs into a caller-supplied buffer. |
| [NdisMRegisterScatterGatherDma function](nf-ndis-ndismregisterscattergatherdma.md) | Bus master miniport drivers call the NdisMRegisterScatterGatherDma function from MiniportInitializeEx to initialize a scatter/gather DMA channel. |
| [NdisFreeNetBuffer function](nf-ndis-ndisfreenetbuffer.md) | Call the NdisFreeNetBuffer function to free a NET_BUFFER structure that was previously allocated from a NET_BUFFER structure pool with the NdisAllocateNetBuffer function. |
| [NdisWriteErrorLogEntry function](nf-ndis-ndiswriteerrorlogentry.md) | NdisWriteErrorLogEntry writes an entry to the system I/O error log file. |
| [NdisDprFreePacketNonInterlocked function](nf-ndis-ndisdprfreepacketnoninterlocked.md) | TBD |
| [NDIS_GET_NET_BUFFER_LIST_GFT_OFFLOAD_VPORT_ID function](nf-ndis-ndis-get-net-buffer-list-gft-offload-vport-id.md) | TBD |
| [NdisGetPhysicalAddressLow function](nf-ndis-ndisgetphysicaladdresslow.md) | NdisGetPhysicalAddressLow returns the low-order part of a given physical address. |
| [NET_BUFFER_LIST_SET_HASH_VALUE function](nf-ndis-net-buffer-list-set-hash-value.md) | TBD |
| [NET_BUFFER_DATA_OFFSET function](nf-ndis-net-buffer-data-offset.md) | TBD |
| [NdisAllocateMdl function](nf-ndis-ndisallocatemdl.md) | The NdisAllocateMdl function allocates an MDL that describes the memory buffer at the specified virtual address. |
| [NdisMCmAddPartyComplete function](nf-ndis-ndismcmaddpartycomplete.md) | NdisMCmAddPartyComplete returns the final status of a client's request, for which the MCM driver previously returned NDIS_STATUS_PENDING, to add a party on an established multipoint VC. |
| [NdisFPauseComplete function](nf-ndis-ndisfpausecomplete.md) | A filter driver must call the NdisFPauseComplete function to complete a pause operation if the driver returned NDIS_STATUS_PENDING from its FilterPause function. |
| [NdisAllocateNetBufferListContext function](nf-ndis-ndisallocatenetbufferlistcontext.md) | Call the NdisAllocateNetBufferListContext function to allocate more context space in the NET_BUFFER_LIST_CONTEXT structure of a NET_BUFFER_LIST structure. |
| [NdisMAllocateMapRegisters function](nf-ndis-ndismallocatemapregisters.md) | TBD |
| [NdisInterlockedPushEntrySList function](nf-ndis-ndisinterlockedpushentryslist.md) | The NdisInterlockedPushEntrySList function inserts an entry at the head of a sequenced, singly linked list. |
| [NdisGetHypervisorInfo function](nf-ndis-ndisgethypervisorinfo.md) | Important  Starting with Windows 10 Version 1703, NdisGetHypervisorInfo is deprecated and should not be used. |
| [NdisMCreateLog function](nf-ndis-ndismcreatelog.md) | NdisMCreateLog allocates and opens a log file in which a miniport driver can write data to be displayed by a driver-dedicated Win32 application. |
| [NDIS_TEST_RECEIVE_FLAG function](nf-ndis-ndis-test-receive-flag.md) | TBD |
| [NdisWriteRegisterUshort function](nf-ndis-ndiswriteregisterushort.md) | NdisWriteRegisterUshort is called by the miniport driver to write a USHORT to a memory-mapped device register. |
| [NdisRawWritePortUshort function](nf-ndis-ndisrawwriteportushort.md) | NdisRawWritePortUshort writes a USHORT value to an I/O port on the NIC. |
| [FILTER_SYNCHRONOUS_OID_REQUEST_COMPLETE function](nf-ndis-filter-synchronous-oid-request-complete.md) | TBD |
| [NdisMResetComplete function](nf-ndis-ndismresetcomplete~r1.md) | The NdisMResetComplete function returns the final status of a reset request for which the miniport driver previously returned NDIS_STATUS_PENDING. |
| [NdisGetPhysicalAddressHigh function](nf-ndis-ndisgetphysicaladdresshigh.md) | NdisGetPhysicalAddressHigh returns the high-order part of a given physical address. |
| [NdisCoAssignInstanceName function](nf-ndis-ndiscoassigninstancename.md) | NdisCoAssignInstanceName assigns an instance name to a VC and causes NDIS to register a GUID (globally unique identifier) for the assigned name with Windows Management Instrumentation (WMI). |
| [NdisCloseAdapterEx function](nf-ndis-ndiscloseadapterex.md) | A protocol driver calls the NdisCloseAdapterEx function to release the binding and the resources that were allocated when the driver called the NdisOpenAdapterEx function. |
| [NDIS_SET_PACKET_STATUS function](nf-ndis-ndis-set-packet-status.md) | TBD |
| [NdisInterlockedInsertTailList function](nf-ndis-ndisinterlockedinserttaillist.md) | The NdisInterlockedInsertTailList function inserts an entry, usually a packet, at the tail of a doubly linked list so that access to the list is synchronized in a multiprocessor-safe way. |
| [NdisAllocateTimerObject function](nf-ndis-ndisallocatetimerobject.md) | The NdisAllocateTimerObject function allocates and initializes a timer object for use with subsequent NdisXxx timer functions. |
| [NDIS_GET_PACKET_STATUS function](nf-ndis-ndis-get-packet-status.md) | TBD |
| [NdisUnchainBufferAtBack function](nf-ndis-ndisunchainbufferatback.md) | TBD |
| [NdisMPciAssignResources function](nf-ndis-ndismpciassignresources.md) | TBD |
| [NdisGetDeviceReservedExtension function](nf-ndis-ndisgetdevicereservedextension.md) | The NdisGetDeviceReservedExtension function gets a pointer to the device extension that is associated with a device object. |
| [NdisMDeregisterScatterGatherDma function](nf-ndis-ndismderegisterscattergatherdma.md) | Bus-master miniport drivers call NdisMDeregisterScatterGatherDma to release DMA resources that were allocated with the NdisMRegisterScatterGatherDma function. |
| [NdisAdjustBufferLength function](nf-ndis-ndisadjustbufferlength.md) | TBD |
| [NdisCancelTimer function](nf-ndis-ndiscanceltimer.md) | TBD |
| [NDIS_SET_PACKET_TIME_SENT function](nf-ndis-ndis-set-packet-time-sent.md) | TBD |
| [NdisMUnmapIoSpace function](nf-ndis-ndismunmapiospace.md) | NdisMUnmapIoSpace releases a virtual range mapped by an initialization-time call to NdisMMapIoSpace. |
| [NdisCoRequest function](nf-ndis-ndiscorequest.md) | TBD |
| [NdisChainBufferAtBack function](nf-ndis-ndischainbufferatback.md) | TBD |
| [NdisReleaseReadWriteLock function](nf-ndis-ndisreleasereadwritelock.md) | The NdisReleaseReadWriteLock function releases a lock that was acquired in a preceding call to NdisAcquireReadWriteLock.Note  The read-write lock interface is deprecated for NDIS 6.20 and later drivers, which should use NdisReleaseRWLock instead of NdisReleaseReadWriteLock. |
| [NdisDeregisterProtocol function](nf-ndis-ndisderegisterprotocol.md) | TBD |
| [NdisFreeBufferPool function](nf-ndis-ndisfreebufferpool.md) | TBD |
| [NDIS_DECLARE_SHARED_MEMORY_PROVIDER_CONTEXT function](nf-ndis-ndis-declare-shared-memory-provider-context.md) | TBD |
| [NdisQueryMdlOffset function](nf-ndis-ndisquerymdloffset.md) | TBD |
| [NET_BUFFER_CHECKSUM_BIAS function](nf-ndis-net-buffer-checksum-bias.md) | TBD |
| [NDIS_SET_PACKET_TIME_RECEIVED function](nf-ndis-ndis-set-packet-time-received.md) | TBD |
| [NdisClIncomingCallComplete function](nf-ndis-ndisclincomingcallcomplete.md) | NdisClIncomingCallComplete returns a client's acceptance or rejection of an offered incoming call, for which the client's ProtocolClIncomingCall function previously returned NDIS_STATUS_PENDING. |
| [NdisMEnableVirtualization function](nf-ndis-ndismenablevirtualization.md) | A miniport driver calls the NdisMEnableVirtualization function during the creation or deletion of a NIC switch on the network adapter. |
| [NdisAllocateMemory function](nf-ndis-ndisallocatememory.md) | TBD |
| [NDIS_GET_PACKET_HEADER_SIZE function](nf-ndis-ndis-get-packet-header-size.md) | TBD |
| [NdisFreeRWLock function](nf-ndis-ndisfreerwlock.md) | The NdisFreeRWLock function frees a read/write lock that was previously allocated with the NdisAllocateRWLock function. |
| [NET_BUFFER_CURRENT_MDL_OFFSET function](nf-ndis-net-buffer-current-mdl-offset.md) | TBD |
| [NdisFreePacketPool function](nf-ndis-ndisfreepacketpool.md) | TBD |
| [NdisFreeTimerObject function](nf-ndis-ndisfreetimerobject.md) | The NdisFreeTimerObject function frees a timer object that was allocated with the NdisAllocateTimerObject function. |
| [NdisClModifyCallQoS function](nf-ndis-ndisclmodifycallqos.md) | NdisClModifyCallQoS requests a change in the quality of service on a connection. |
| [NdisMCmNotifyCloseAddressFamily function](nf-ndis-ndismcmnotifycloseaddressfamily.md) | The NdisMCmNotifyCloseAddressFamily function notifies NDIS that a specified address family (AF) that is associated with a miniport call manager (MCM) should be closed and NDIS should notify any affected CoNDIS clients. |
| [NBL_CLEAR_FLAG function](nf-ndis-nbl-clear-flag.md) | TBD |
| [NdisMRestartComplete function](nf-ndis-ndismrestartcomplete.md) | A miniport driver must call the NdisMRestartComplete function to complete a restart operation if the driver returned NDIS_STATUS_PENDING from its MiniportRestart function. |
| [NDIS_WAIT_FOR_MUTEX function](nf-ndis-ndis-wait-for-mutex.md) | TBD |
| [NdisClNotifyCloseAddressFamilyComplete function](nf-ndis-ndisclnotifycloseaddressfamilycomplete.md) | The NdisClNotifyCloseAddressFamilyComplete function returns the final status of an address family (AF) close operation for which the caller's ProtocolClNotifyCloseAf function returned NDIS_STATUS_PENDING. |
| [NET_BUFFER_LIST_RECEIVE_QUEUE_ID function](nf-ndis-net-buffer-list-receive-queue-id.md) | TBD |
| [NDIS_GET_NET_BUFFER_LIST_IM_RESERVED function](nf-ndis-ndis-get-net-buffer-list-im-reserved.md) | TBD |
| [NDIS_TEST_CLONE_FLAG function](nf-ndis-ndis-test-clone-flag.md) | TBD |
| [NdisGetPacketCancelId function](nf-ndis-ndisgetpacketcancelid.md) | TBD |
| [NdisMAllocateSharedMemoryAsyncEx function](nf-ndis-ndismallocatesharedmemoryasyncex.md) | Miniport drivers call the NdisMAllocateSharedMemoryAsyncEx function to allocate additional memory shared between the driver and its bus-master DMA NIC, usually when the miniport driver is running low on available NIC receive buffers. |
| [NBL_SET_FLAG function](nf-ndis-nbl-set-flag.md) | TBD |
| [NdisClDropParty function](nf-ndis-ndiscldropparty.md) | NdisClDropParty drops a party from the client's multipoint VC. |
| [NDIS_STRING_CONST function](nf-ndis-ndis-string-const.md) | TBD |
| [NdisMWriteLogData function](nf-ndis-ndismwritelogdata.md) | NdisMWriteLogData transfers driver-supplied information into the log file for consumption and display by a driver-dedicated Win32 application. |
| [NdisMReadConfigBlock function](nf-ndis-ndismreadconfigblock.md) | A miniport driver for a PCI Express (PCIe) Virtual Function (VF) calls the NdisMReadConfigBlock function to read data from a VF configuration block. |
| [NdisAdvanceNetBufferListDataStart function](nf-ndis-ndisadvancenetbufferlistdatastart.md) | Call the NdisAdvanceNetBufferListDataStart function to release data space that was claimed in previous calls to the NdisRetreatNetBufferListDataStart function. |
| [NDIS_TEST_SEND_AT_DISPATCH_LEVEL function](nf-ndis-ndis-test-send-at-dispatch-level.md) | TBD |
| [NdisIfGetInterfaceIndexFromNetLuid function](nf-ndis-ndisifgetinterfaceindexfromnetluid.md) | The NdisIfGetInterfaceIndexFromNetLuid function gets the network interface index that is associated with a NET_LUID value. |
| [NdisInterlockedAddUlong function](nf-ndis-ndisinterlockedaddulong.md) | The NdisInterlockedAddUlong function adds an unsigned long value to a given unsigned integer as an atomic operation, using a caller-supplied spin lock to synchronize access to the integer variable. |
| [NdisQueryPacket function](nf-ndis-ndisquerypacket.md) | TBD |
| [NdisMFreeSharedMemory function](nf-ndis-ndismfreesharedmemory.md) | NdisMFreeSharedMemory frees memory that was previously allocated by NdisMAllocateSharedMemory or NdisMAllocateSharedMemoryAsyncEx by the driver of a DMA NIC. |
| [NDIS_NBL_GET_MEDIA_SPECIFIC_INFO function](nf-ndis-ndis-nbl-get-media-specific-info.md) | TBD |
| [NdisFreeIoWorkItem function](nf-ndis-ndisfreeioworkitem.md) | NDIS drivers call the NdisFreeIoWorkItem function to free a specified work item. |
| [NdisFCancelDirectOidRequest function](nf-ndis-ndisfcanceldirectoidrequest.md) | Filter drivers call the NdisFCancelDirectOidRequest function to cancel a previous direct OID request to the underlying drivers. |
| [NDIS_RELEASE_MUTEX function](nf-ndis-ndis-release-mutex.md) | TBD |
| [NDIS_MDL_TO_SPAN_PAGES function](nf-ndis-ndis-mdl-to-span-pages.md) | TBD |
| [NET_BUFFER_LIST_DUP_ACK_COUNT function](nf-ndis-net-buffer-list-dup-ack-count.md) | TBD |
| [NDIS_STATUS_INDICATION_CLEAR_FLAG function](nf-ndis-ndis-status-indication-clear-flag.md) | TBD |
| [NdisOpenFile function](nf-ndis-ndisopenfile.md) | The NdisOpenFile function returns a handle for an opened file. |
| [NdisMCoIndicateReceivePacket function](nf-ndis-ndismcoindicatereceivepacket.md) | TBD |
| [NET_BUFFER_SCATTER_GATHER_LIST function](nf-ndis-net-buffer-scatter-gather-list.md) | TBD |
| [NdisStoreUlong function](nf-ndis-ndisstoreulong.md) | The NdisStoreUlong function stores a ULONG value at a particular address, avoiding alignment faults. |
| [NdisGetDataBuffer function](nf-ndis-ndisgetdatabuffer.md) | Call the NdisGetDataBuffer function to gain access to a contiguous block of data from a NET_BUFFER structure. |
| [NdisReadConfiguration function](nf-ndis-ndisreadconfiguration.md) | The NdisReadConfiguration function returns the value of a named entry of the specified type from the registry, given the handle to an open registry key. |
| [NdisMCompleteDmaTransfer function](nf-ndis-ndismcompletedmatransfer.md) | The NdisMCompleteDmaTransfer function indicates that a system DMA transfer operation has completed. It resets the system DMA controller in preparation for further DMA transfers. |
| [NdisCompleteNetPnPEvent function](nf-ndis-ndiscompletenetpnpevent.md) | Protocol drivers call the NdisCompleteNetPnPEvent function to complete a response to a Plug and Play or Power Management event for which the caller's ProtocolNetPnPEvent function returned NDIS_STATUS_PENDING. |
| [NDIS_CLEAR_SEND_FLAG function](nf-ndis-ndis-clear-send-flag.md) | TBD |
| [NET_BUFFER_LIST_NEXT_NBL function](nf-ndis-net-buffer-list-next-nbl.md) | TBD |
| [NdisCmModifyCallQoSComplete function](nf-ndis-ndiscmmodifycallqoscomplete.md) | NdisCmModifyCallQoSComplete indicates the completion of the client's request, for which the call manager previously returned NDIS_STATUS_PENDING, to modify the quality of service on a VC. |
| [NdisGetCurrentProcessorCounts function](nf-ndis-ndisgetcurrentprocessorcounts.md) | The NdisGetCurrentProcessorCounts function returns counts for the current processor that a driver can use to determine CPU usage for a particular time interval. |
| [NET_BUFFER_FIRST_MDL function](nf-ndis-net-buffer-first-mdl.md) | TBD |
| [NdisMQueryInformationComplete function](nf-ndis-ndismqueryinformationcomplete.md) | TBD |
| [NDIS_SET_NET_BUFFER_LIST_GFT_OFFLOAD_FLAGS function](nf-ndis-ndis-set-net-buffer-list-gft-offload-flags.md) | TBD |
| [NdisIMInitializeDeviceInstanceEx function](nf-ndis-ndisiminitializedeviceinstanceex.md) | The NdisIMInitializeDeviceInstanceEx function initiates the initialization operation for a virtual miniport and optionally sets up state information about the virtual miniport for subsequently bound protocol drivers. |
| [NdisReinitializePacket function](nf-ndis-ndisreinitializepacket.md) | TBD |
| [NdisMCoReceiveComplete function](nf-ndis-ndismcoreceivecomplete.md) | TBD |
| [NdisDeregisterProtocolDriver function](nf-ndis-ndisderegisterprotocoldriver.md) | A protocol driver calls the NdisDeregisterProtocolDriver function to release the resources that NDIS allocated when the driver called the NdisRegisterProtocolDriver function. |
| [NdisGetReceivedPacket function](nf-ndis-ndisgetreceivedpacket.md) | TBD |
| [NdisMDeregisterDevice function](nf-ndis-ndismderegisterdevice.md) | TBD |
| [NdisCompleteBindAdapterEx function](nf-ndis-ndiscompletebindadapterex.md) | A protocol driver calls the NdisCompleteBindAdapterEx function to complete a binding operation for which the driver's ProtocolBindAdapterEx function returned NDIS_STATUS_PENDING. |
| [NdisRegisterDeviceEx function](nf-ndis-ndisregisterdeviceex.md) | The NdisRegisterDeviceEx function creates a device object that is based upon the specified attributes. |
| [NdisInitializeTimer function](nf-ndis-ndisinitializetimer.md) | TBD |
| [NdisQueryAdapterInstanceName function](nf-ndis-ndisqueryadapterinstancename.md) | The NdisQueryAdapterInstanceName function retrieves the friendly name of a physical NIC or a virtual adapter that the calling protocol driver is bound to. |
| [NdisMRegisterIoPortRange function](nf-ndis-ndismregisterioportrange.md) | NdisMRegisterIoPortRange sets up driver access to device I/O ports with the NdisRawReadPortXxx and NdisRawWritePortXxx functions and claims the range of I/O port addresses in the registry for that driver's NIC. |
| [NET_BUFFER_LIST_FLAGS function](nf-ndis-net-buffer-list-flags.md) | TBD |
| [NdisActiveGroupCount function](nf-ndis-ndisactivegroupcount.md) | The NdisActiveGroupCount function returns the number of processor groups that are currently active in the local computer system. |
| [NdisMCmOidRequest function](nf-ndis-ndismcmoidrequest.md) | The NdisMCmOidRequest function sends an OID request from a miniport call manager (MCM) driver to a CoNDIS client. |
| [NdisSetPeriodicTimer function](nf-ndis-ndissetperiodictimer.md) | TBD |
| [NDIS_SET_PACKET_HEADER_SIZE function](nf-ndis-ndis-set-packet-header-size.md) | TBD |
| [NdisMUpdateSharedMemory function](nf-ndis-ndismupdatesharedmemory.md) | TBD |
| [NdisCoRequestComplete function](nf-ndis-ndiscorequestcomplete.md) | TBD |
| [NdisMCmModifyCallQoSComplete function](nf-ndis-ndismcmmodifycallqoscomplete.md) | NdisMCmModifyCallQoSComplete indicates the completion of the client's request, for which the MCM driver previously returned NDIS_STATUS_PENDING, to modify the quality of service on a VC. |
| [NdisMEthIndicateReceive function](nf-ndis-ndismethindicatereceive.md) | TBD |
| [NdisMSetAttributesEx function](nf-ndis-ndismsetattributesex.md) | TBD |
| [DECLARE_NDIS_HANDLE function](nf-ndis-declare-ndis-handle~r4.md) | TBD |
| [NdisClCloseCall function](nf-ndis-ndisclclosecall.md) | NdisClCloseCall requests that a call on the specified VC be torn down. |
| [NdisSetNetBufferListProtocolId function](nf-ndis-ndissetnetbufferlistprotocolid.md) | TBD |
| [NdisGetDriverHandle function](nf-ndis-ndisgetdriverhandle.md) | TBD |
| [NDIS_GET_NET_BUFFER_LIST_CANCEL_ID function](nf-ndis-ndis-get-net-buffer-list-cancel-id.md) | TBD |
| [NDIS_PAGEABLE_FUNCTION function](nf-ndis-ndis-pageable-function.md) | TBD |
| [NdisMConfigMSIXTableEntry function](nf-ndis-ndismconfigmsixtableentry.md) | The NdisMConfigMSIXTableEntry function performs configuration operations for MSI-X table entries for device-assigned MSI-X messages. |
| [NET_BUFFER_LIST_GET_HASH_VALUE function](nf-ndis-net-buffer-list-get-hash-value.md) | TBD |
| [NdisMCmRegisterSapComplete function](nf-ndis-ndismcmregistersapcomplete.md) | NdisMCmRegisterSapComplete returns the final status of a client's request, for which the MCM driver's ProtocolCmRegisterSap function previously returned NDIS_STATUS_PENDING, to register a SAP. |
| [NdisWriteEventLogEntry function](nf-ndis-ndiswriteeventlogentry.md) | NdisWriteEventLogEntry logs an event to the Win32 event log. |
| [NdisGetFirstBufferFromPacket function](nf-ndis-ndisgetfirstbufferfrompacket.md) | TBD |
| [NdisMPauseComplete function](nf-ndis-ndismpausecomplete.md) | A miniport driver must call the NdisMPauseComplete function to complete a pause operation if the driver returned NDIS_STATUS_PENDING from its MiniportPause function. |
| [NdisAllocateGenericObject function](nf-ndis-ndisallocategenericobject.md) | Components that do not have an NDIS handle use the NdisAllocateGenericObject function to allocate a generic NDIS object. |
| [NdisIMGetDeviceContext function](nf-ndis-ndisimgetdevicecontext.md) | TBD |
| [NdisScheduleWorkItem function](nf-ndis-ndisscheduleworkitem.md) | TBD |
| [NdisInitializeWrapper function](nf-ndis-ndisinitializewrapper.md) | TBD |
| [NdisAllocateCloneNetBufferList function](nf-ndis-ndisallocateclonenetbufferlist.md) | Call the NdisAllocateCloneNetBufferList function to create a new clone NET_BUFFER_LIST structure. |
| [NDIS_DECLARE_CO_CM_AF_CONTEXT function](nf-ndis-ndis-declare-co-cm-af-context.md) | TBD |
| [NdisMCmDeregisterSapComplete function](nf-ndis-ndismcmderegistersapcomplete.md) | NdisMCmDeregisterSapComplete returns the final status of a client's request, for which the MCM driver previously returned NDIS_STATUS_PENDING, to deregister a SAP. |
| [NdisMAllocateSharedMemory function](nf-ndis-ndismallocatesharedmemory.md) | NdisMAllocateSharedMemory allocates and maps a host memory range so that the memory range is simultaneously accessible from both the host system and a DMA NIC. |
| [NdisRawWritePortBufferUshort function](nf-ndis-ndisrawwriteportbufferushort.md) | NdisRawWritePortBufferUshort writes a specified number of USHORT values from a caller-supplied buffer to a given I/O port. |
| [NDIS_PHYSICAL_ADDRESS_CONST function](nf-ndis-ndis-physical-address-const.md) | TBD |
| [NDIS_GET_PACKET_CANCEL_ID function](nf-ndis-ndis-get-packet-cancel-id.md) | TBD |
| [NET_BUFFER_LIST_GET_HASH_FUNCTION function](nf-ndis-net-buffer-list-get-hash-function.md) | TBD |
| [NdisMCmOidRequestComplete function](nf-ndis-ndismcmoidrequestcomplete.md) | The NdisMCmOidRequestComplete function returns the final status of a CoNDIS OID requestthat a miniport call manager (MCM) driver's ProtocolCoOidRequest function previously returned NDIS_STATUS_PENDING for. |
| [NdisMCmCloseCallComplete function](nf-ndis-ndismcmclosecallcomplete.md) | NdisMCmCloseCallComplete returns the final status of a client's request, for which the MCM driver previously returned NDIS_STATUS_PENDING, to tear down a call. |
| [NdisFreeScatterGatherList function](nf-ndis-ndisfreescattergatherlist.md) | The NdisFreeScatterGatherList function frees a scatter/gather list. |
| [NdisAllocateNetBufferListPool function](nf-ndis-ndisallocatenetbufferlistpool.md) | Call the NdisAllocateNetBufferListPool function to allocate a pool of NET_BUFFER_LIST structures. |
| [NdisIMDeInitializeDeviceInstance function](nf-ndis-ndisimdeinitializedeviceinstance.md) | The NdisIMDeInitializeDeviceInstance function calls an NDIS intermediate driver's MiniportHaltEx function to tear down the driver's virtual miniport. |
| [NdisEqualUnicodeString function](nf-ndis-ndisequalunicodestring.md) | The NdisEqualUnicodeString function compares two Unicode strings and returns whether they are equal. |
| [NdisDeregisterDeviceEx function](nf-ndis-ndisderegisterdeviceex.md) | The NdisDeregisterDeviceEx function removes, from the system, a device object that was created by the NdisRegisterDeviceEx function. |
| [NdisMIndicateReceivePacket function](nf-ndis-ndismindicatereceivepacket.md) | TBD |
| [NdisSystemActiveProcessorCount function](nf-ndis-ndissystemactiveprocessorcount.md) | The NdisSystemActiveProcessorCount function returns the number of currently active processors in the local computer. |
| [NdisSendPackets function](nf-ndis-ndissendpackets.md) | TBD |
| [NdisMRegisterInterruptEx function](nf-ndis-ndismregisterinterruptex.md) | NDIS miniport drivers call the NdisMRegisterInterruptEx function to register an interrupt. |
| [NDIS_DECLARE_MINIPORT_SGLIST_CONTEXT function](nf-ndis-ndis-declare-miniport-sglist-context.md) | TBD |
| [NdisAnsiStringToUnicodeString function](nf-ndis-ndisansistringtounicodestring.md) | The NdisAnsiStringToUnicodeString function converts a given counted ANSI string into a counted Unicode string. The translation conforms to the current system locale information. |
| [NdisDprAcquireReadWriteLock function](nf-ndis-ndisdpracquirereadwritelock.md) | The NdisDprAcquireReadWriteLock function acquires a lock that the caller uses for either write or read access to the resources that are shared among driver threads.Note  The read-write lock interface is deprecated for NDIS 6.20 and later drivers, which should use NdisAcquireRWLockRead or NdisAcquireRWLockWrite (setting NDIS_RWL_AT_DISPATCH_LEVEL in the Flags parameter) instead of NdisDprAcquireReadWriteLock. |
| [NdisQueryBindInstanceName function](nf-ndis-ndisquerybindinstancename.md) | The NdisQueryBindInstanceName function retrieves the friendly name of a physical NIC or a virtual adapter that the calling protocol driver will bind to. |
| [NdisMCmMakeCallComplete function](nf-ndis-ndismcmmakecallcomplete.md) | NdisMCmMakeCallComplete returns the final status of a client's request, for which the MCM driver previously returned NDIS_STATUS_PENDING, to make an outgoing call. |
| [NDIS_SET_PACKET_CANCEL_ID function](nf-ndis-ndis-set-packet-cancel-id.md) | TBD |
| [NET_BUFFER_CURRENT_MDL function](nf-ndis-net-buffer-current-mdl.md) | TBD |
| [NdisMSleep function](nf-ndis-ndismsleep.md) | The NdisMSleep function delays execution of the caller for a given interval in microseconds. |
| [NdisSetupDmaTransfer function](nf-ndis-ndissetupdmatransfer.md) | TBD |
| [NdisMGetDeviceProperty function](nf-ndis-ndismgetdeviceproperty.md) | The NdisMGetDeviceProperty function retrieves device objects required to set up communication with a miniport driver through a bus driver. |
| [NdisMCoOidRequestComplete function](nf-ndis-ndismcooidrequestcomplete.md) | The NdisMCoOidRequestComplete function returns the final status of an OID requestthat a miniport driver's MiniportCoOidRequest function returned NDIS_STATUS_PENDING for. |
| [NdisOpenProtocolConfiguration function](nf-ndis-ndisopenprotocolconfiguration.md) | TBD |
| [NdisWritePciSlotInformation function](nf-ndis-ndiswritepcislotinformation.md) | TBD |
| [NdisAcquireReadWriteLock function](nf-ndis-ndisacquirereadwritelock.md) | The NdisAcquireReadWriteLock function acquires a lock that the caller uses for either write or read access to the resources that are shared among driver threads.Note  The read-write lock interface is deprecated for NDIS 6.20 and later drivers, which should use NdisAcquireRWLockRead or NdisAcquireRWLockWrite instead of NdisAcquireReadWriteLock. |
| [NdisFreeCloneOidRequest function](nf-ndis-ndisfreecloneoidrequest.md) | The NdisFreeCloneOidRequest function frees a cloned NDIS_OID_REQUEST structure. |
| [NdisSetCoalescableTimerObject function](nf-ndis-ndissetcoalescabletimerobject.md) | The NdisSetCoalescableTimerObject function sets a timer object that the operating system coordinates with other timers, typically to reduce power consumption, when the exact expiration of the timer is not important to driver operation. |
| [NdisGetMdlPhysicalArraySize function](nf-ndis-ndisgetmdlphysicalarraysize.md) | TBD |
| [NdisRegisterTdiCallBack function](nf-ndis-ndisregistertdicallback.md) | TBD |
| [NdisPacketSize function](nf-ndis-ndispacketsize.md) | TBD |
| [NdisFRestartComplete function](nf-ndis-ndisfrestartcomplete.md) | A filter driver must call the NdisFRestartComplete function to complete a restart operation if the driver returned NDIS_STATUS_PENDING from its FilterRestart function. |
| [NdisMRemoveMiniport function](nf-ndis-ndismremoveminiport.md) | The NdisMRemoveMiniport function removes the specified miniport driver adapter that the miniport driver has determined is unrecoverable from the system. |
| [NDIS_DECLARE_PROTOCOL_OPEN_CONTEXT function](nf-ndis-ndis-declare-protocol-open-context.md) | TBD |
| [NDIS_PACKET_LAST_NDIS_BUFFER function](nf-ndis-ndis-packet-last-ndis-buffer.md) | TBD |
| [NdisReleaseSpinLock function](nf-ndis-ndisreleasespinlock.md) | The NdisReleaseSpinLock function releases a spin lock that was acquired in a preceding call to the NdisAcquireSpinLock function. |
| [NdisInterlockedPushEntryList function](nf-ndis-ndisinterlockedpushentrylist.md) | TBD |
| [NdisMStartBufferPhysicalMapping function](nf-ndis-ndismstartbufferphysicalmapping.md) | TBD |
| [NDIS_INIT_MUTEX function](nf-ndis-ndis-init-mutex.md) | TBD |
| [NdisDprReleaseReadWriteLock function](nf-ndis-ndisdprreleasereadwritelock.md) | The NdisDprReleaseReadWriteLock function releases a lock that was acquired in a preceding call to NdisDprAcquireReadWriteLock.Note  The read-write lock interface is deprecated for NDIS 6.20 and later drivers, which should use NdisReleaseRWLock instead of NdisDprReleaseReadWriteLock. |
| [NdisReadPcmciaAttributeMemory function](nf-ndis-ndisreadpcmciaattributememory.md) | TBD |
| [NdisRegisterProtocolDriver function](nf-ndis-ndisregisterprotocoldriver.md) | A protocol driver calls the NdisRegisterProtocolDriver function to register its ProtocolXxx functions with NDIS. |
| [NdisCmMakeCallComplete function](nf-ndis-ndiscmmakecallcomplete.md) | NdisCmMakeCallComplete returns the final status of a client's request, for which the call manager previously returned NDIS_STATUS_PENDING, to make an outgoing call. |
| [NdisWaitEvent function](nf-ndis-ndiswaitevent.md) | The NdisWaitEvent function puts the caller into a wait state until the given event is set to the Signaled state or the wait times out. |
| [NET_BUFFER_PROTOCOL_RESERVED function](nf-ndis-net-buffer-protocol-reserved.md) | TBD |
| [NdisGetPoolFromNetBufferList function](nf-ndis-ndisgetpoolfromnetbufferlist.md) | Call the NdisGetPoolFromNetBufferList function to get the NET_BUFFER_LIST structure pool handle that is associated with a specified NET_BUFFER_LIST structure. |
| [NdisEqualString function](nf-ndis-ndisequalstring.md) | The NdisEqualString function compares two strings, in the OS-default character set, to determine whether they are equal. |
| [NdisMWriteConfigBlock function](nf-ndis-ndismwriteconfigblock.md) | A miniport driver for a PCI Express (PCIe) Virtual Function (VF) calls the NdisMWriteConfigBlock function to write data to a VF configuration block. |
| [NdisCmDispatchIncomingDropParty function](nf-ndis-ndiscmdispatchincomingdropparty.md) | NdisCmDispatchIncomingDropParty notifies a client that it should remove a particular party on a multipoint VC, usually because the call manager has received a request over the network to close an active multipoint connection. |
| [NdisMSetMiniportSecondary function](nf-ndis-ndismsetminiportsecondary.md) | TBD |
| [NDIS_SET_ORIGINAL_PACKET function](nf-ndis-ndis-set-original-packet.md) | TBD |
| [NDIS_TEST_RECEIVE_CANNOT_PEND function](nf-ndis-ndis-test-receive-cannot-pend.md) | TBD |
| [NdisSetProtocolFilter function](nf-ndis-ndissetprotocolfilter.md) | TBD |
| [NdisIMCancelInitializeDeviceInstance function](nf-ndis-ndisimcancelinitializedeviceinstance.md) | The NdisIMCancelInitializeDeviceInstance function cancels a preceding call to the NdisIMInitializeDeviceInstanceEx function. |
| [NdisClDeregisterSap function](nf-ndis-ndisclderegistersap.md) | NdisClDeregisterSap releases a previously registered SAP. |
| [NdisCompletePnPEvent function](nf-ndis-ndiscompletepnpevent.md) | TBD |
| [NDIS_TEST_RETURN_AT_DISPATCH_LEVEL function](nf-ndis-ndis-test-return-at-dispatch-level.md) | TBD |
| [NdisMCoSendComplete function](nf-ndis-ndismcosendcomplete.md) | TBD |
| [NdisMCmRequestComplete function](nf-ndis-ndismcmrequestcomplete.md) | TBD |
| [NdisInterlockedRemoveHeadList function](nf-ndis-ndisinterlockedremoveheadlist.md) | The NdisInterlockedRemoveHeadList function removes an entry, usually a packet, from the head of a doubly linked list so that access to the list is synchronized in a multiprocessor-safe way. |
| [NdisMDeregisterDmaChannel function](nf-ndis-ndismderegisterdmachannel.md) | The NdisMDeregisterDmaChannel function releases a miniport driver's claim on a DMA channel for a NIC. |
| [NdisMRegisterMiniportDriver function](nf-ndis-ndismregisterminiportdriver.md) | A miniport driver calls the NdisMRegisterMiniportDriver function to register MiniportXxx entry points with NDIS as the first step in initialization. |
| [NdisMPromoteMiniport function](nf-ndis-ndismpromoteminiport.md) | TBD |
| [NdisMSetVirtualFunctionBusData function](nf-ndis-ndismsetvirtualfunctionbusdata.md) | A miniport driver calls the NdisMSetVirtualFunctionBusData function to write data to the PCI Express (PCIe) configuration space of a Virtual Function (VF) on the network adapter. |
| [NdisMGetVirtualFunctionLocation function](nf-ndis-ndismgetvirtualfunctionlocation.md) | A miniport driver calls the NdisMGetVirtualFunctionLocation function to query the device location of a PCI Express (PCIe) Virtual Function (VF) on a PCI bus. The driver uses the device location to construct the PCIe Requestor ID (RID) for the VF. |
| [NBL_TEST_PROT_RSVD_FLAG function](nf-ndis-nbl-test-prot-rsvd-flag.md) | TBD |
| [NdisMCmDispatchCallConnected function](nf-ndis-ndismcmdispatchcallconnected.md) | NdisMCmDispatchCallConnected notifies NDIS and the client that data transfers can begin on a VC that the MCM driver created for an incoming call initiated on a remote node. |
| [NdisIMDeregisterLayeredMiniport function](nf-ndis-ndisimderegisterlayeredminiport.md) | TBD |
| [NdisMWanIndicateReceiveComplete function](nf-ndis-ndismwanindicatereceivecomplete.md) | TBD |
| [NdisMCmDispatchIncomingCall function](nf-ndis-ndismcmdispatchincomingcall.md) | NdisMCmDispatchIncomingCall informs the client of an incoming call on a SAP previously registered by that client with the MCM driver. |
| [NdisFSendNetBufferLists function](nf-ndis-ndisfsendnetbufferlists.md) | Filter drivers call the NdisFSendNetBufferLists function to send a list of network data buffers. |
| [NdisFreeReassembledNetBufferList function](nf-ndis-ndisfreereassemblednetbufferlist.md) | Call the NdisFreeReassembledNetBufferList function to free a reassembled NET_BUFFER_LIST structure and the associated NET_BUFFER structure and MDL chain. |
| [NdisTransferData function](nf-ndis-ndistransferdata.md) | TBD |
| [NDIS_SET_CLONE_FLAG function](nf-ndis-ndis-set-clone-flag.md) | TBD |
| [NdisFillMemory function](nf-ndis-ndisfillmemory.md) | The NdisFillMemory function fills a caller-supplied buffer with the given character. |
| [NDIS_GET_PACKET_PROTOCOL_TYPE function](nf-ndis-ndis-get-packet-protocol-type.md) | TBD |
| [NdisRawReadPortBufferUchar function](nf-ndis-ndisrawreadportbufferuchar.md) | NdisRawReadPortBufferUchar reads a specified number of bytes into a caller-supplied buffer. |
| [NET_BUFFER_SHARED_MEM_HANDLE function](nf-ndis-net-buffer-shared-mem-handle.md) | TBD |
| [NdisMoveFromMappedMemory function](nf-ndis-ndismovefrommappedmemory.md) | TBD |
| [NdisAllocatePacketPoolEx function](nf-ndis-ndisallocatepacketpoolex.md) | TBD |
| [NdisCmNotifyCloseAddressFamily function](nf-ndis-ndiscmnotifycloseaddressfamily.md) | The NdisCmNotifyCloseAddressFamily function notifies NDIS that a call manager is unbinding from an underlying miniport adapter and that any associated CoNDIS clients should close the specified address family (AF). |
| [NdisCmAddPartyComplete function](nf-ndis-ndiscmaddpartycomplete.md) | NdisCmAddPartyComplete returns the final status of a client's request, for which the call manager previously returned NDIS_STATUS_PENDING, to add a party on an established multipoint VC. |
| [NdisFreeNetBufferPool function](nf-ndis-ndisfreenetbufferpool.md) | Call the NdisFreeNetBufferPool function to free NET_BUFFER structure pools that are created with the NdisAllocateNetBufferPool function. |
| [NDIS_PER_PACKET_INFO_FROM_PACKET function](nf-ndis-ndis-per-packet-info-from-packet.md) | TBD |
| [NdisClOpenAddressFamilyEx function](nf-ndis-ndisclopenaddressfamilyex.md) | The NdisClOpenAddressFamilyEx function registers an address family (AF) that is associated with a call manager for a connection-oriented client. |
| [NdisDeregisterTdiCallBack function](nf-ndis-ndisderegistertdicallback.md) | TBD |
| [NdisInitializeReadWriteLock function](nf-ndis-ndisinitializereadwritelock.md) | The NdisInitializeReadWriteLock function initializes a read or write lock variable of type NDIS_RW_LOCK.Note  The read-write lock interface is deprecated for NDIS 6.20 and later drivers, which should use NdisAllocateRWLock instead of NdisInitializeReadWriteLock. |
| [NdisCmCloseAddressFamilyComplete function](nf-ndis-ndiscmcloseaddressfamilycomplete.md) | NdisCmCloseAddressFamilyComplete returns the final status of a client's request, for which the CM's ProtocolCmCloseAf function returned NDIS_STATUS_PENDING, to close the AF. |
| [NdisBufferVirtualAddress function](nf-ndis-ndisbuffervirtualaddress.md) | TBD |
| [NdisRawReadPortUchar function](nf-ndis-ndisrawreadportuchar.md) | NdisRawReadPortUchar reads a byte from a given I/O port on the NIC. |
| [NdisIMCopySendPerPacketInfo function](nf-ndis-ndisimcopysendperpacketinfo.md) | TBD |
| [NdisSetSendFlags function](nf-ndis-ndissetsendflags.md) | TBD |
| [NdisClRegisterSap function](nf-ndis-ndisclregistersap.md) | NdisClRegisterSap registers a SAP on which the client can receive incoming calls from a remote node. |
| [NdisRawReadPortUlong function](nf-ndis-ndisrawreadportulong.md) | NdisRawReadPortUlong reads a ULONG value from a given I/O port on the NIC. |
| [NdisMRegisterMiniport function](nf-ndis-ndismregisterminiport.md) | TBD |
| [NdisCmDispatchIncomingCall function](nf-ndis-ndiscmdispatchincomingcall.md) | NdisCmDispatchIncomingCall informs the client of an incoming call on a SAP previously registered by that client. |
| [NdisGetNextMdl function](nf-ndis-ndisgetnextmdl.md) | TBD |
| [NDIS_SET_SEND_FLAG function](nf-ndis-ndis-set-send-flag.md) | TBD |
| [NdisCancelTimerObject function](nf-ndis-ndiscanceltimerobject.md) | The NdisCancelTimerObject function cancels a timer object that is associated with a previous call to the NdisSetTimerObject function. |
| [NdisFreeString function](nf-ndis-ndisfreestring.md) | The NdisFreeString function releases storage that was allocated by NdisInitializeString for a buffered string. |
| [NdisFlushBuffer function](nf-ndis-ndisflushbuffer.md) | TBD |
| [NdisQueryPendingIOCount function](nf-ndis-ndisquerypendingiocount.md) | TBD |
| [NdisMCompleteBufferPhysicalMapping function](nf-ndis-ndismcompletebufferphysicalmapping.md) | TBD |
| [NdisFDirectOidRequestComplete function](nf-ndis-ndisfdirectoidrequestcomplete.md) | Filter drivers call the NdisFDirectOidRequestComplete function to return the final status of a direct OID request for which the driver's FilterDirectOidRequest function returned NDIS_STATUS_PENDING. |
| [NDIS_DECLARE_SHARED_MEMORY_ALLOCATION_CONTEXT function](nf-ndis-ndis-declare-shared-memory-allocation-context.md) | TBD |
| [NdisMWanIndicateReceive function](nf-ndis-ndismwanindicatereceive.md) | TBD |
| [NdisMDeregisterInterruptEx function](nf-ndis-ndismderegisterinterruptex.md) | Miniport drivers call NdisMDeregisterInterruptEx to release resources that were previously allocated with the NdisMRegisterInterruptEx function. |
| [NdisInitializeListHead function](nf-ndis-ndisinitializelisthead.md) | The NdisInitializeListHead function initializes a doubly linked, driver-maintained queue. |
| [NDIS_NBL_ADD_MEDIA_SPECIFIC_INFO function](nf-ndis-ndis-nbl-add-media-specific-info.md) | TBD |
| [NdisFreeMemory function](nf-ndis-ndisfreememory.md) | The NdisFreeMemory function releases a block of memory that was previously allocated with the NdisAllocateMemoryWithTagPriority function. |
| [NdisMQueryProbedBars function](nf-ndis-ndismqueryprobedbars.md) | A miniport driver calls the NdisMQueryProbedBars function to obtain the values of a network adapter's PCI Express (PCIe) Base Address Registers (BARs). |
| [NdisGetRoutineAddress function](nf-ndis-ndisgetroutineaddress.md) | The NdisGetRoutineAddress function returns the address of a routine given the routine's name. |
| [NDIS_STATUS_INDICATION_SET_FLAG function](nf-ndis-ndis-status-indication-set-flag.md) | TBD |
| [NdisReadRegisterUlong function](nf-ndis-ndisreadregisterulong.md) | NdisReadRegisterUlong is called by the miniport driver to read a ULONG from a memory-mapped device register. |
| [NdisRetreatNetBufferDataStart function](nf-ndis-ndisretreatnetbufferdatastart.md) | Call the NdisRetreatNetBufferDataStart function to access more used data space in the MDL chain of a NET_BUFFER structure. |
| [NdisOidRequest function](nf-ndis-ndisoidrequest.md) | The NdisOidRequest function forwards a request to the underlying drivers to query the capabilities or status of an adapter or set the state of an adapter. |
| [NDIS_SET_SEND_COMPLETE_FLAG function](nf-ndis-ndis-set-send-complete-flag.md) | TBD |
| [NDIS_DECLARE_MINIPORT_INTERRUPT_CONTEXT function](nf-ndis-ndis-declare-miniport-interrupt-context.md) | TBD |
| [NdisDprAcquireSpinLock function](nf-ndis-ndisdpracquirespinlock.md) | The NdisDprAcquireSpinLock function acquires a spin lock so the caller can synchronize access to resources shared among non-ISR driver functions in a multiprocessor-safe way. |
| [NdisRawWritePortBufferUlong function](nf-ndis-ndisrawwriteportbufferulong.md) | NdisRawWritePortBufferUlong writes a specified number of ULONG values from a caller-supplied buffer to a given I/O port. |
| [NdisIfRegisterProvider function](nf-ndis-ndisifregisterprovider.md) | The NdisIfRegisterProvider function registers an NDIS network interface provider. |
| [NdisMGetBusData function](nf-ndis-ndismgetbusdata.md) | NDIS drivers call the NdisMGetBusData function to read the configuration space of a device. |
| [NdisMQueueDpcEx function](nf-ndis-ndismqueuedpcex.md) | NDIS miniport drivers call the NdisMQueueDpcEx function to schedule DPC calls on CPUs. |
| [NdisFSendNetBufferListsComplete function](nf-ndis-ndisfsendnetbufferlistscomplete.md) | Filter drivers call the NdisFSendNetBufferListsComplete function to return a linked list of NET_BUFFER_LIST structures to an overlying driver and to return the final status of a send request. |
| [NdisWriteConfiguration function](nf-ndis-ndiswriteconfiguration.md) | The NdisWriteConfiguration function writes a caller-supplied value for a specified entry into the registry. This function must be invoked serially with respect to itself and the NdisReadConfiguration function. |
| [NdisAllocateMemoryWithTagPriority function](nf-ndis-ndisallocatememorywithtagpriority.md) | NDIS drivers call the NdisAllocateMemoryWithTagPriority function to allocate a pool of memory from the non-paged pool. |
| [NET_BUFFER_LIST_SWITCH_FORWARDING_DETAIL function](nf-ndis-net-buffer-list-switch-forwarding-detail.md) | TBD |
| [NdisInterlockedAddLargeStatistic function](nf-ndis-ndisinterlockedaddlargestatistic.md) | The NdisInterlockedAddLargeStatistic function performs an interlocked addition of a ULONG increment value to a LARGE_INTEGER addend value. |
| [NdisIfGetNetLuidFromInterfaceIndex function](nf-ndis-ndisifgetnetluidfrominterfaceindex.md) | The NdisIfGetNetLuidFromInterfaceIndex function gets the NET_LUID value that is associated with a network interface index. |
| [NdisCreateLookaheadBufferFromSharedMemory function](nf-ndis-ndiscreatelookaheadbufferfromsharedmemory.md) | TBD |
| [NdisCompleteBindAdapter function](nf-ndis-ndiscompletebindadapter.md) | TBD |
| [NdisReturnNetBufferLists function](nf-ndis-ndisreturnnetbufferlists.md) | NDIS drivers call the NdisReturnNetBufferLists function to release ownership of a list of NET_BUFFER_LIST structures, along with the associated NET_BUFFER structures and network data. |
| [NdisMCoIndicateStatus function](nf-ndis-ndismcoindicatestatus.md) | TBD |
| [NdisIfDeregisterProvider function](nf-ndis-ndisifderegisterprovider.md) | The NdisIfDeregisterProvider function deregisters an interface provider that was previously registered by a call to the NdisIfRegisterProvider function. |
| [NdisFOidRequestComplete function](nf-ndis-ndisfoidrequestcomplete.md) | Filter drivers call the NdisFOidRequestComplete function to return the final status of an OID request for which the driver's FilterOidRequest function returned NDIS_STATUS_PENDING. |
| [NdisAcquireSpinLock function](nf-ndis-ndisacquirespinlock.md) | The NdisAcquireSpinLock function acquires a spin lock so the caller gains exclusive access to the resources, shared among driver functions, that the spin lock protects. |
| [NdisResetEvent function](nf-ndis-ndisresetevent.md) | The NdisResetEvent function clears the Signaled state of a given event. |
| [NdisCopyBuffer function](nf-ndis-ndiscopybuffer.md) | TBD |
| [NBL_TEST_PROTOCOL_RSVD_FLAG function](nf-ndis-nbl-test-protocol-rsvd-flag.md) | TBD |
| [NdisIfQueryBindingIfIndex function](nf-ndis-ndisifquerybindingifindex.md) | The NdisIfQueryBindingIfIndex function retrieves the network interface indexes and NET_LUID values for the highest and lowest layered network interfaces that are associated with a specified protocol binding. |
| [NdisMCancelTimer function](nf-ndis-ndismcanceltimer.md) | TBD |
| [NdisDprFreePacket function](nf-ndis-ndisdprfreepacket.md) | TBD |
| [NdisCoOidRequest function](nf-ndis-ndiscooidrequest.md) | The NdisCoOidRequest function forwards a request to targeted CoNDIS drivers to query or set OID-specified information of the target driver. |
| [NdisIMCopySendCompletePerPacketInfo function](nf-ndis-ndisimcopysendcompleteperpacketinfo.md) | TBD |
| [NdisFreeSharedMemory function](nf-ndis-ndisfreesharedmemory.md) | The NdisFreeSharedMemory function frees shared memory that a driver allocated from a shared memory provider. |
| [NdisQueryBufferOffset function](nf-ndis-ndisquerybufferoffset.md) | TBD |
| [NDIS_DECLARE_CO_CL_AF_CONTEXT function](nf-ndis-ndis-declare-co-cl-af-context.md) | TBD |
| [NET_BUFFER_LIST_CONTEXT_DATA_START function](nf-ndis-net-buffer-list-context-data-start.md) | TBD |
| [NdisMDeregisterInterrupt function](nf-ndis-ndismderegisterinterrupt.md) | TBD |
| [NdisMInvalidateConfigBlock function](nf-ndis-ndisminvalidateconfigblock.md) | A miniport driver calls the NdisMInvalidateConfigBlock function to notify NDIS that the data for one or more Virtual Function (VF) configuration blocks has been changed. |
| [NdisEqualMemory function](nf-ndis-ndisequalmemory.md) | The NdisEqualMemory function compares a specified number of characters in one block of memory with the same number of characters in a second block of memory. |
| [NBL_SET_PROTOCOL_RSVD_FLAG function](nf-ndis-nbl-set-protocol-rsvd-flag.md) | TBD |
| [NdisCompleteDmaTransfer function](nf-ndis-ndiscompletedmatransfer.md) | TBD |
| [NdisMIndicateReceiveNetBufferLists function](nf-ndis-ndismindicatereceivenetbufferlists.md) | Miniport drivers call the NdisMIndicateReceiveNetBufferLists function to indicate the receipt of data from the network. |
| [NdisGroupActiveProcessorMask function](nf-ndis-ndisgroupactiveprocessormask.md) | The NdisGroupActiveProcessorMask function returns the currently active processor mask for the specified group. |
| [NET_BUFFER_MINIPORT_RESERVED function](nf-ndis-net-buffer-miniport-reserved.md) | TBD |
| [NdisSetPacketCancelId function](nf-ndis-ndissetpacketcancelid.md) | TBD |
| [NDIS_SET_PACKET_TIME_TO_SEND function](nf-ndis-ndis-set-packet-time-to-send.md) | TBD |
| [NdisSystemProcessorCount function](nf-ndis-ndissystemprocessorcount.md) | The NdisSystemProcessorCount function determines whether the caller is running on a uniprocessor or multiprocessor computer. |
| [NDIS_NBL_REMOVE_MEDIA_SPECIFIC_INFO_EX function](nf-ndis-ndis-nbl-remove-media-specific-info-ex.md) | TBD |
| [NDIS_SET_RETURN_FLAG function](nf-ndis-ndis-set-return-flag.md) | TBD |
| [NdisAllocateRWLock function](nf-ndis-ndisallocaterwlock.md) | The NdisAllocateRWLock function allocates a read/write lock variable of type NDIS_RW_LOCK_EX. |
| [NdisUnicodeStringToAnsiString function](nf-ndis-ndisunicodestringtoansistring.md) | The NdisUnicodeStringToAnsiString function converts a given counted Unicode string into a counted ANSI string. The translation conforms to the current system locale information. |
| [NdisAcquireRWLockRead function](nf-ndis-ndisacquirerwlockread.md) | The NdisAcquireRWLockRead function obtains a read lock that the caller uses for read access to resources that are shared among driver threads. |
| [WanMiniportSend function](nf-ndis-wanminiportsend.md) | TBD |
| [NDIS_TEST_SEND_COMPLETE_AT_DISPATCH_LEVEL function](nf-ndis-ndis-test-send-complete-at-dispatch-level.md) | TBD |
| [NdisGetSystemUpTime function](nf-ndis-ndisgetsystemuptime.md) | TBD |
| [NET_BUFFER_LIST_RECEIVE_FILTER_ID function](nf-ndis-net-buffer-list-receive-filter-id.md) | TBD |
| [NdisMSetupDmaTransfer function](nf-ndis-ndismsetupdmatransfer.md) | The NdisMSetupDmaTransfer function sets up the host DMA controller for a DMA transfer. |
| [NET_BUFFER_LIST_CONTEXT_DATA_SIZE function](nf-ndis-net-buffer-list-context-data-size.md) | TBD |
| [NdisGetPoolFromPacket function](nf-ndis-ndisgetpoolfrompacket.md) | TBD |
| [NDIS_SET_NET_BUFFER_LIST_VIRTUAL_SUBNET_ID function](nf-ndis-ndis-set-net-buffer-list-virtual-subnet-id.md) | TBD |
| [NET_BUFFER_LIST_NBL_FLAGS function](nf-ndis-net-buffer-list-nbl-flags.md) | TBD |
| [NdisCompleteUnbindAdapter function](nf-ndis-ndiscompleteunbindadapter.md) | TBD |
| [NdisGetProcessorInformation function](nf-ndis-ndisgetprocessorinformation.md) | The NdisGetProcessorInformation function retrieves information about the CPU topology of the local computer and the set of processors that a miniport driver must use for receive side scaling (RSS). |
| [NET_BUFFER_LIST_MINIPORT_RESERVED function](nf-ndis-net-buffer-list-miniport-reserved.md) | TBD |
| [NdisMSetPeriodicTimer function](nf-ndis-ndismsetperiodictimer.md) | TBD |
| [NdisMTrIndicateReceiveComplete function](nf-ndis-ndismtrindicatereceivecomplete.md) | TBD |
| [NdisMRegisterUnloadHandler function](nf-ndis-ndismregisterunloadhandler.md) | TBD |
| [NdisInterlockedIncrement function](nf-ndis-ndisinterlockedincrement.md) | The NdisInterlockedIncrement function increments a caller-supplied variable as an atomic operation. |
| [NdisMOidRequestComplete function](nf-ndis-ndismoidrequestcomplete.md) | Miniport drivers call the NdisMOidRequestComplete function to return the final status of an OID request for which the driver's MiniportOidRequest function returned NDIS_STATUS_PENDING. |
| [NdisMCmDispatchIncomingCloseCall function](nf-ndis-ndismcmdispatchincomingclosecall.md) | NdisMCmDispatchIncomingCloseCall tells a client to tear down an active or offered call, usually because the MCM driver has received a request from the network to close the connection. |
| [DECLARE_NDIS_HANDLE function](nf-ndis-declare-ndis-handle~r3.md) | TBD |
| [NdisZeroMappedMemory function](nf-ndis-ndiszeromappedmemory.md) | NdisZeroMappedMemory fills a block of memory that was mapped with a preceding call to NdisMMapIoSpace with zeros. |
| [NdisMFreePort function](nf-ndis-ndismfreeport.md) | The NdisMFreePort function frees an NDIS port that was previously allocated with the NdisMAllocatePort function. |
| [NdisClMakeCall function](nf-ndis-ndisclmakecall.md) | NdisClMakeCall sets up an outgoing call on a client-created VC. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [FILTER_ATTACH callback](nc-ndis-filter-attach.md) | NDIS calls a filter driver's FilterAttach function to allocate and initialize a filter module's data structures.Note  You must declare the function by using the FILTER_ATTACH type. |
| [NDIS_M_STATUS_HANDLER callback function](nc-ndis-ndis-m-status-handler.md) | TBD |
| [PROTOCOL_CL_REGISTER_SAP_COMPLETE callback](nc-ndis-protocol-cl-register-sap-complete.md) | A connection-oriented NDIS client that accepts incoming calls must have a ProtocolClRegisterSapComplete function to complete the asynchronous operations that it initiates with NdisClRegisterSap. |
| [FILTER_DIRECT_OID_REQUEST callback](nc-ndis-filter-direct-oid-request.md) | NDIS calls a filter driver's FilterDirectOidRequest function to process a direct OID request that is associated with the specified filter module.Note  You must declare the function by using the FILTER_DIRECT_OID_REQUEST type. |
| [MINIPORT_CO_SEND_NET_BUFFER_LISTS callback](nc-ndis-miniport-co-send-net-buffer-lists.md) | The MiniportCoSendNetBufferLists function transmits network data that is contained in a specified linked list of NET_BUFFER_LIST structures.Note  You must declare the function by using the MINIPORT_CO_SEND_NET_BUFFER_LISTS type. |
| [NDIS_PD_QUEUE_CONTROL callback function](nc-ndis-ndis-pd-queue-control.md) | TBD |
| [NDIS_M_SEND_COMPLETE_HANDLER callback function](nc-ndis-ndis-m-send-complete-handler.md) | TBD |
| [NDIS_SWITCH_SET_NET_BUFFER_LIST_SOURCE callback](nc-ndis-ndis-switch-set-net-buffer-list-source.md) | The SetNetBufferListSource function sets the Hyper-V extensible switch source port identifier and network adapter index for a packet that is specified by a NET_BUFFER_LIST structure. |
| [NDIS_PD_CLEAR_RECEIVE_FILTER callback](nc-ndis-ndis-pd-clear-receive-filter.md) | The PacketDirect (PD) platform calls a PD-capable miniport driver's NdisPDClearReceiveFilter function to clear this filter from the PD platform. |
| [SEND_HANDLER callback function](nc-ndis-send-handler.md) | TBD |
| [PROTOCOL_BIND_ADAPTER_EX callback](nc-ndis-protocol-bind-adapter-ex.md) | NDIS calls a protocol driver's ProtocolBindAdapterEx function to request the driver to bind to a miniport adapter.Note  You must declare the function by using the PROTOCOL_BIND_ADAPTER_EX type. |
| [NDIS_PD_RELEASE_RECEIVE_QUEUES callback function](nc-ndis-ndis-pd-release-receive-queues.md) | TBD |
| [CO_REQUEST_COMPLETE_HANDLER callback function](nc-ndis-co-request-complete-handler.md) | TBD |
| [MINIPORT_INTERRUPT_DPC callback](nc-ndis-miniport-interrupt-dpc.md) | A miniport driver must provide a MiniportInterruptDPC function if the driver calls the NdisMRegisterInterruptEx function to register an interrupt. |
| [PNP_EVENT_HANDLER callback function](nc-ndis-pnp-event-handler.md) | TBD |
| [FILTER_SET_MODULE_OPTIONS callback function](nc-ndis-filter-set-module-options.md) | TBD |
| [NDIS_PD_PROVIDER_CONTROL callback function](nc-ndis-ndis-pd-provider-control.md) | TBD |
| [MINIPORT_RESTART callback](nc-ndis-miniport-restart.md) | The MiniportRestart function initiates a restart request for a miniport adapter that is paused. |
| [TRANSFER_DATA_COMPLETE_HANDLER callback function](nc-ndis-transfer-data-complete-handler.md) | TBD |
| [NDIS_M_START_SENDS callback function](nc-ndis-ndis-m-start-sends.md) | TBD |
| [PROTOCOL_CO_DELETE_VC callback](nc-ndis-protocol-co-delete-vc.md) | The ProtocolCoDeleteVc function is required. |
| [MINIPORT_ENABLE_INTERRUPT callback](nc-ndis-miniport-enable-interrupt.md) | NDIS can call a miniport driver's MiniportEnableInterruptEx handler to enable interrupts for diagnostic and troubleshooting purposes. |
| [PROTOCOL_CM_REG_SAP callback](nc-ndis-protocol-cm-reg-sap.md) | The ProtocolCmRegisterSap function is a required function that is called by NDIS to request that a call manager register a SAP (service access point) on behalf of a connection-oriented client.Note  You must declare the function by using the PROTOCOL_CM_REG_SAP type. For more information, see the following Examples section. |
| [NDIS_SWITCH_ADD_NET_BUFFER_LIST_DESTINATION callback](nc-ndis-ndis-switch-add-net-buffer-list-destination.md) | The AddNetBufferListDestination function adds a single destination port for a packet that is specified by a NET_BUFFER_LIST structure. |
| [PROTOCOL_CM_CLOSE_AF callback](nc-ndis-protocol-cm-close-af.md) | The ProtocolCmCloseAf function is a required function that releases per-open resources for an address family that a call manager supports.Note  You must declare the function by using the PROTOCOL_CM_CLOSE_AF type. |
| [MINIPORT_CANCEL_SEND callback](nc-ndis-miniport-cancel-send.md) | NDIS calls a miniport driver's MiniportCancelSend function to cancel the transmission of all NET_BUFFER_LIST structures that are marked with a specified cancellation identifier. |
| [WAN_RECEIVE_HANDLER callback function](nc-ndis-wan-receive-handler.md) | TBD |
| [FILTER_PACKET_INDICATION_HANDLER callback function](nc-ndis-filter-packet-indication-handler.md) | TBD |
| [MINIPORT_ISR callback](nc-ndis-miniport-isr.md) | NDIS calls the MiniportInterrupt function when a NIC, or another device that shares the interrupt with the NIC, generates an interrupt. |
| [PROTOCOL_CM_ACTIVATE_VC_COMPLETE callback](nc-ndis-protocol-cm-activate-vc-complete.md) | The ProtocolCmActivateVcComplete function is required. |
| [NDIS_PROC_CALLBACK callback function](nc-ndis-ndis-proc-callback.md) | TBD |
| [STATUS_HANDLER callback function](nc-ndis-status-handler.md) | TBD |
| [MINIPORT_HALT callback](nc-ndis-miniport-halt.md) | NDIS calls a miniport driver's MiniportHaltEx function to free resources when a miniport adapter is removed, and to stop the hardware. |
| [MINIPORT_DISABLE_MESSAGE_INTERRUPT callback](nc-ndis-miniport-disable-message-interrupt.md) | NDIS can call a miniport driver's MiniportDisableMessageInterrupt handler to disable a message interrupt for diagnostic and troubleshooting purposes. |
| [IF_QUERY_OBJECT callback function](nc-ndis-if-query-object.md) | TBD |
| [NDIS_SWITCH_SET_NET_BUFFER_LIST_SWITCH_CONTEXT callback](nc-ndis-ndis-switch-set-net-buffer-list-switch-context.md) | The Hyper-V extensible switch extension calls the SetNetBufferListSwitchContext function to attach an extension-allocated context buffer to the NET_BUFFER_LIST. |
| [WAN_RCV_COMPLETE_HANDLER callback function](nc-ndis-wan-rcv-complete-handler.md) | TBD |
| [CLOSE_ADAPTER_COMPLETE_HANDLER callback function](nc-ndis-close-adapter-complete-handler.md) | TBD |
| [RESET_COMPLETE_HANDLER callback function](nc-ndis-reset-complete-handler.md) | TBD |
| [MINIPORT_CO_DEACTIVATE_VC callback](nc-ndis-miniport-co-deactivate-vc.md) | The MiniportCoDeactivateVc function is required for connection-oriented miniports. |
| [FILTER_STATUS callback](nc-ndis-filter-status.md) | The FilterStatus function indicates status changes that are reported by NDIS or an underlying driver.Note  You must declare the function by using the FILTER_STATUS type. |
| [MINIPORT_CO_OID_REQUEST callback](nc-ndis-miniport-co-oid-request.md) | The MiniportCoOidRequest function handles an OID request to query or set information in CoNDIS miniport driver.Note  You must declare the function by using the MINIPORT_CO_OID_REQUEST type. |
| [NET_BUFFER_ALLOCATE_MDL_HANDLER callback](nc-ndis-net-buffer-allocate-mdl-handler.md) | The NetAllocateMdl function allocates an MDL with an associated memory block of a specified size. |
| [MINIPORT_ADD_DEVICE callback](nc-ndis-miniport-add-device.md) | The MiniportAddDevice function enables a miniport driver to establish a context area for an added device. |
| [PROTOCOL_NET_PNP_EVENT callback](nc-ndis-protocol-net-pnp-event.md) | NDIS calls the ProtocolNetPnPEvent function to indicate a network Plug and Play event, an NDIS PnP event, or a power management event to a protocol driver.Note  You must declare the function by using the PROTOCOL_NET_PNP_EVENT type. |
| [RESET_HANDLER callback function](nc-ndis-reset-handler.md) | TBD |
| [W_PNP_EVENT_NOTIFY_HANDLER callback function](nc-ndis-w-pnp-event-notify-handler.md) | TBD |
| [PROTOCOL_CL_ADD_PARTY_COMPLETE callback](nc-ndis-protocol-cl-add-party-complete.md) | The ProtocolClAddPartyComplete function is required for connection-oriented NDIS clients that set up multipoint connections. |
| [FILTER_SEND_NET_BUFFER_LISTS callback](nc-ndis-filter-send-net-buffer-lists.md) | NDIS calls the FilterSendNetBufferLists function to allow a filter driver to filter a linked list of NET_BUFFER_LIST structures.Note  You must declare the function by using the FILTER_SEND_NET_BUFFER_LISTS type. |
| [WAN_TRANSFER_DATA_COMPLETE_HANDLER callback function](nc-ndis-wan-transfer-data-complete-handler.md) | TBD |
| [W_CANCEL_SEND_PACKETS_HANDLER callback function](nc-ndis-w-cancel-send-packets-handler.md) | TBD |
| [FILTER_PAUSE callback](nc-ndis-filter-pause.md) | NDIS calls a filter driver's FilterPause function to initiate a pause operation for the specified filter module.Note  You must declare the function by using the FILTER_PAUSE type. |
| [NDIS_SWITCH_GET_NET_BUFFER_LIST_DESTINATIONS callback](nc-ndis-ndis-switch-get-net-buffer-list-destinations.md) | The GetNetBufferListDestinations function returns the Hyper-V extensible switch destination ports of a packet that is specified by a NET_BUFFER_LIST structure. |
| [MINIPORT_OID_REQUEST callback](nc-ndis-miniport-oid-request.md) | NDIS calls a miniport driver's MiniportOidRequest function to handle an OID request to query or set information in the driver. |
| [FILTER_OID_REQUEST callback](nc-ndis-filter-oid-request.md) | NDIS calls a filter driver's FilterOidRequest function to process an OID request that is associated with the specified filter module.Note  You must declare the function by using the FILTER_OID_REQUEST type. |
| [NET_BUFFER_FREE_MDL_HANDLER callback](nc-ndis-net-buffer-free-mdl-handler.md) | The NetFreeMdl function frees an MDL that was previously allocated by the NetAllocateMdl function. |
| [NDIS_PD_SET_RECEIVE_FILTER callback](nc-ndis-ndis-pd-set-receive-filter.md) | The PacketDirect (PD) platform calls a PD-capable miniport driver's NdisPDSetReceiveFilter function to direct specific flows of packets to a specific PD receive queue. |
| [PROTOCOL_CO_OID_REQUEST callback](nc-ndis-protocol-co-oid-request.md) | The ProtocolCoOidRequest function handles OID requests that CoNDIS clients or stand-alone call managers initiate by calls to the NdisCoOidRequest function or that a miniport call manager (MCM) driver initiates by calls to the NdisMCmOidRequest function.Note  You must declare the function by using the PROTOCOL_CO_OID_REQUEST type. For more information, see the following Examples section. |
| [MINIPORT_ENABLE_MESSAGE_INTERRUPT callback](nc-ndis-miniport-enable-message-interrupt.md) | NDIS can call a miniport driver's MiniportEnableMessageInterrupt function to enable a message interrupt for diagnostic and troubleshooting purposes. |
| [W_SEND_HANDLER callback function](nc-ndis-w-send-handler.md) | TBD |
| [PROTOCOL_STATUS_EX callback](nc-ndis-protocol-status-ex.md) | The ProtocolStatusEx function indicates status-changes from underlying connectionless drivers or NDIS.Note  You must declare the function by using the PROTOCOL_STATUS_EX type. |
| [WM_SEND_HANDLER callback function](nc-ndis-wm-send-handler.md) | TBD |
| [RECEIVE_HANDLER callback function](nc-ndis-receive-handler.md) | TBD |
| [PROTOCOL_CO_STATUS_EX callback](nc-ndis-protocol-co-status-ex.md) | The ProtocolCoStatusEx function indicates status changes from underlying connection-oriented drivers or from NDIS.Note  You must declare the function by using the PROTOCOL_CO_STATUS_EX type. |
| [PROTOCOL_CM_MODIFY_QOS_CALL callback](nc-ndis-protocol-cm-modify-qos-call.md) | The ProtocolCmModifyCallQoS function is required. |
| [NDIS_PD_QUERY_COUNTER callback](nc-ndis-ndis-pd-query-counter.md) | The PacketDirect (PD) platform calls a PD-capable miniport driver's NdisPDQueryCounter function to query the current values stored in a counter object. |
| [PROTOCOL_CM_DEREGISTER_SAP callback](nc-ndis-protocol-cm-deregister-sap.md) | The ProtocolCmDeregisterSap function is required. |
| [PROTOCOL_CL_OPEN_AF_COMPLETE callback function](nc-ndis-protocol-cl-open-af-complete.md) | TBD |
| [W_HALT_HANDLER callback function](nc-ndis-w-halt-handler.md) | TBD |
| [MINIPORT_IDLE_NOTIFICATION callback](nc-ndis-miniport-idle-notification.md) | NDIS calls the MiniportIdleNotification handler function to start the NDIS selective suspend operation on an idle network adapter. Through this operation, the network adapter is suspended and transitioned to a low-power state. |
| [SEND_COMPLETE_HANDLER callback function](nc-ndis-send-complete-handler.md) | TBD |
| [MINIPORT_CANCEL_DIRECT_OID_REQUEST callback](nc-ndis-miniport-cancel-direct-oid-request.md) | NDIS calls a miniport driver's MiniportCancelDirectOidRequest function to cancel a direct OID request. |
| [ALLOCATE_SHARED_MEMORY_HANDLER callback](nc-ndis-allocate-shared-memory-handler.md) | The NetAllocateSharedMemory function (ALLOCATE_SHARED_MEMORY_HANDLER entry point) is called by NDIS when a driver allocates shared memory from a shared memory provider. |
| [FILTER_RETURN_NET_BUFFER_LISTS callback](nc-ndis-filter-return-net-buffer-lists.md) | NDIS calls the FilterReturnNetBufferLists function to return a linked list of NET_BUFFER_LIST structures and associated data to a filter driver.Note  You must declare the function by using the FILTER_RETURN_NET_BUFFER_LISTS type. |
| [PROTOCOL_DIRECT_OID_REQUEST_COMPLETE callback](nc-ndis-protocol-direct-oid-request-complete.md) | The ProtocolDirectOidRequestComplete function completes the processing of a protocol driver-initiated direct OID request for which the NdisDirectOidRequest function returned NDIS_STATUS_PENDING.Note  You must declare the function by using the PROTOCOL_DIRECT_OID_REQUEST_COMPLETE type. For more information, see the following Examples section. |
| [NDIS_SWITCH_COPY_NET_BUFFER_LIST_INFO callback](nc-ndis-ndis-switch-copy-net-buffer-list-info.md) | The Hyper-V extensible switch extension calls the CopyNetBufferListInfo function to copy the out-of-band (OOB) forwarding context from a source packet's NET_BUFFER_LIST structure to a destination packet's NET_BUFFER_LIST structure. |
| [MINIPORT_UNLOAD callback](nc-ndis-miniport-unload.md) | NDIS calls a miniport driver's MiniportDriverUnload function to request the driver to release resources before the system completes a driver unload operation. |
| [WAN_SEND_HANDLER callback function](nc-ndis-wan-send-handler.md) | TBD |
| [W_DISABLE_INTERRUPT_HANDLER callback function](nc-ndis-w-disable-interrupt-handler.md) | TBD |
| [NDIS_PD_ALLOCATE_QUEUE callback](nc-ndis-ndis-pd-allocate-queue.md) | The PacketDirect (PD) platform calls a PD-capable miniport driver's NdisPDAllocateQueue function to allocate a queue. |
| [PROTOCOL_CLOSE_ADAPTER_COMPLETE_EX callback](nc-ndis-protocol-close-adapter-complete-ex.md) | NDIS calls a protocol driver's ProtocolCloseAdapterCompleteEx function to complete a close adapter operation for which the NdisCloseAdapterEx function returned NDIS_STATUS_PENDING.Note  You must declare the function by using the PROTOCOL_CLOSE_ADAPTER_COMPLETE_EX type. For more information, see the following Examples section. |
| [PROTOCOL_CL_DEREGISTER_SAP_COMPLETE callback](nc-ndis-protocol-cl-deregister-sap-complete.md) | The ProtocolClDeregisterSapComplete function is used by connection-oriented NDIS clients. |
| [NDIS_SWITCH_FREE_NET_BUFFER_LIST_FORWARDING_CONTEXT callback](nc-ndis-ndis-switch-free-net-buffer-list-forwarding-context.md) | The FreeNetBufferListForwardingContext function releases resources in the out-of-band (OOB) extensible switch forwarding context of a NET_BUFFER_LIST structure. |
| [IF_SET_OBJECT callback function](nc-ndis-if-set-object.md) | TBD |
| [W_SEND_PACKETS_HANDLER callback function](nc-ndis-w-send-packets-handler.md) | TBD |
| [PROTOCOL_CL_INCOMING_CALL callback](nc-ndis-protocol-cl-incoming-call.md) | The ProtocolClIncomingCall function is used by connection-oriented clients that accept incoming calls. |
| [PROTOCOL_CL_MAKE_CALL_COMPLETE callback](nc-ndis-protocol-cl-make-call-complete.md) | The ProtocolClMakeCallComplete function is used by connection-oriented NDIS clients that make outgoing calls. |
| [UNLOAD_PROTOCOL_HANDLER callback function](nc-ndis-unload-protocol-handler.md) | TBD |
| [WAN_RCV_HANDLER callback function](nc-ndis-wan-rcv-handler.md) | TBD |
| [FILTER_RESTART callback](nc-ndis-filter-restart.md) | The FilterRestart function initiates a restart operation for the specified filter module.Note  You must declare the function by using the FILTER_RESTART type. |
| [PROTOCOL_CM_DROP_PARTY callback](nc-ndis-protocol-cm-drop-party.md) | The ProtocolCmDropParty function is required. |
| [MINIPORT_CO_CREATE_VC callback](nc-ndis-miniport-co-create-vc.md) | The MiniportCoCreateVc function is required for connection-oriented miniports. |
| [NDIS_SWITCH_REFERENCE_SWITCH_PORT callback](nc-ndis-ndis-switch-reference-switch-port.md) | The ReferenceSwitchPort function increments the Hyper-V extensible switch reference counter for an extensible switch port. |
| [MINIPORT_PROCESS_SG_LIST callback](nc-ndis-miniport-process-sg-list.md) | A bus-master miniport driver provides a MiniportProcessSGList function to process scatter/gather lists for network data. |
| [FILTER_CANCEL_OID_REQUEST callback](nc-ndis-filter-cancel-oid-request.md) | NDIS calls a filter driver's FilterCancelOidRequest function to cancel an OID request.Note  You must declare the function by using the FILTER_CANCEL_OID_REQUEST type. |
| [W_ISR_HANDLER callback function](nc-ndis-w-isr-handler.md) | TBD |
| [NDIS_M_REQ_COMPLETE_HANDLER callback function](nc-ndis-ndis-m-req-complete-handler.md) | TBD |
| [FILTER_SEND_NET_BUFFER_LISTS_COMPLETE callback](nc-ndis-filter-send-net-buffer-lists-complete.md) | NDIS calls the FilterSendNetBufferListsComplete function to complete a send request that a filter driver started by calling the NdisFSendNetBufferLists function.Note  You must declare the function by using the FILTER_SEND_NET_BUFFER_LISTS_COMPLETE type. |
| [CO_REQUEST_HANDLER callback function](nc-ndis-co-request-handler.md) | TBD |
| [SET_OPTIONS callback](nc-ndis-set-options.md) | NDIS calls a protocol driver's ProtocolSetOptions function to allow the protocol driver to register optional services.Note  You must declare the function by using the SET_OPTIONS type. |
| [UNBIND_HANDLER callback function](nc-ndis-unbind-handler.md) | TBD |
| [PROTOCOL_CL_MODIFY_CALL_QOS_COMPLETE callback](nc-ndis-protocol-cl-modify-call-qos-complete.md) | The ProtocolClModifyCallQoSComplete function is used by connection-oriented NDIS clients that can modify the quality of service on a connection dynamically. |
| [PROTOCOL_CM_ADD_PARTY callback](nc-ndis-protocol-cm-add-party.md) | The ProtocolCmAddParty function is a required function. |
| [REQUEST_COMPLETE_HANDLER callback function](nc-ndis-request-complete-handler.md) | TBD |
| [MINIPORT_DISABLE_INTERRUPT callback](nc-ndis-miniport-disable-interrupt.md) | NDIS can call a miniport driver's MiniportDisableInterruptEx handler to disable interrupts for diagnostic and troubleshooting purposes. |
| [W_RECONFIGURE_HANDLER callback function](nc-ndis-w-reconfigure-handler.md) | TBD |
| [W_ENABLE_INTERRUPT_HANDLER callback function](nc-ndis-w-enable-interrupt-handler.md) | TBD |
| [NDIS_M_RESET_COMPLETE_HANDLER callback function](nc-ndis-ndis-m-reset-complete-handler.md) | TBD |
| [W_MINIPORT_SHUTDOWN_HANDLER callback function](nc-ndis-w-miniport-shutdown-handler.md) | TBD |
| [PROTOCOL_CL_CLOSE_AF_COMPLETE callback](nc-ndis-protocol-cl-close-af-complete.md) | The ProtocolClCloseAfComplete function is used by connection-oriented NDIS clients. |
| [MINIPORT_RETURN_NET_BUFFER_LISTS callback](nc-ndis-miniport-return-net-buffer-lists.md) | NDIS calls the MiniportReturnNetBufferLists function to return ownership of NET_BUFFER_LIST structures, associated NET_BUFFER structures, and any attached MDLs to a miniport driver. |
| [NDIS_PD_REQUEST_DRAIN_NOTIFICATION callback function](nc-ndis-ndis-pd-request-drain-notification.md) | TBD |
| [W_CO_REQUEST_HANDLER callback function](nc-ndis-w-co-request-handler.md) | TBD |
| [PROTOCOL_CO_RECEIVE_NET_BUFFER_LISTS callback](nc-ndis-protocol-co-receive-net-buffer-lists.md) | The ProtocolCoReceiveNetBufferLists function processes receive indications from underlying drivers.Note  You must declare the function by using the PROTOCOL_CO_RECEIVE_NET_BUFFER_LISTS type. |
| [MINIPORT_DIRECT_OID_REQUEST callback](nc-ndis-miniport-direct-oid-request.md) | NDIS calls a miniport driver's MiniportDirectOidRequest function to handle a direct OID request to query or set information in the driver. |
| [MINIPORT_CO_DELETE_VC callback](nc-ndis-miniport-co-delete-vc.md) | The MiniportCoDeleteVc function is required for connection-oriented miniports. |
| [PROTOCOL_CM_NOTIFY_CLOSE_AF_COMPLETE callback](nc-ndis-protocol-cm-notify-close-af-complete.md) | The ProtocolCmNotifyCloseAfComplete function indicates that a client has completed the closing of an address family (AF) that a stand-alone call manager or miniport call manager (MCM) started by calling the NdisCmNotifyCloseAddressFamily or NdisMCmNotifyCloseAddressFamily function, respectively.Note  You must declare the function by using the PROTOCOL_CM_NOTIFY_CLOSE_AF_COMPLETE type. For more information, see the following Examples section. |
| [ETH_RCV_INDICATE_HANDLER callback function](nc-ndis-eth-rcv-indicate-handler.md) | TBD |
| [PROTOCOL_CL_NOTIFY_CLOSE_AF callback](nc-ndis-protocol-cl-notify-close-af.md) | The ProtocolClNotifyCloseAf function notifies a CoNDIS client that the client should close the associated address family (AF).Note  You must declare the function by using the PROTOCOL_CL_NOTIFY_CLOSE_AF type. |
| [PROTOCOL_OPEN_ADAPTER_COMPLETE_EX callback](nc-ndis-protocol-open-adapter-complete-ex.md) | NDIS calls a protocol driver's ProtocolOpenAdapterCompleteEx function to complete an open adapter operation for which the NdisOpenAdapterEx function returned NDIS_STATUS_PENDING.Note  You must declare the function by using the PROTOCOL_OPEN_ADAPTER_COMPLETE_EX type. For more information, see the following Examples section. |
| [NDIS_SWITCH_REFERENCE_SWITCH_NIC callback](nc-ndis-ndis-switch-reference-switch-nic.md) | The ReferenceSwitchNic function increments the Hyper-V extensible switch reference counter for a network adapter that is connected to an extensible switch port. |
| [NDIS_TIMER_FUNCTION callback](nc-ndis-ndis-timer-function.md) | The NetTimerCallback function is called by NDIS after a driver sets a one-shot or periodic timer when a timer fires.Note  You must declare the function by using the NDIS_TIMER_FUNCTION type. |
| [NDIS_PD_FREE_COUNTER callback](nc-ndis-ndis-pd-free-counter.md) | The PacketDirect (PD) platform calls a PD-capable miniport driver's NdisPDFreeCounter function to free a counter object. |
| [NDIS_SWITCH_GROW_NET_BUFFER_LIST_DESTINATIONS callback](nc-ndis-ndis-switch-grow-net-buffer-list-destinations.md) | The GrowNetBufferListDestinations function adds space for additional Hyper-V extensible switch destination ports to a packet that is specified by a NET_BUFFER_LIST structure. |
| [PROTOCOL_CL_CALL_CONNECTED callback](nc-ndis-protocol-cl-call-connected.md) | The ProtocolClCallConnected function is used by connection-oriented NDIS clients that accept incoming calls. |
| [W_INITIALIZE_HANDLER callback function](nc-ndis-w-initialize-handler.md) | TBD |
| [PROTOCOL_SEND_NET_BUFFER_LISTS_COMPLETE callback](nc-ndis-protocol-send-net-buffer-lists-complete.md) | The ProtocolSendNetBufferListsComplete function completes a send operation that the protocol driver initiated with a call to the NdisSendNetBufferLists function.Note  You must declare the function by using the PROTOCOL_SEND_NET_BUFFER_LISTS_COMPLETE type. For more information, see the following Examples section. |
| [PROTOCOL_CL_CLOSE_CALL_COMPLETE callback](nc-ndis-protocol-cl-close-call-complete.md) | The ProtocolClCloseCallComplete function is used by connection-oriented NDIS clients. |
| [MINIPORT_SYNCHRONIZE_INTERRUPT callback](nc-ndis-miniport-synchronize-interrupt.md) | A miniport driver must provide a MiniportSynchronizeInterrupt handler if any driver function that runs at less than DIRQL shares resources with the MiniportInterrupt function. |
| [MINIPORT_CHECK_FOR_HANG callback](nc-ndis-miniport-check-for-hang.md) | NDIS calls a miniport driver's MiniportCheckForHangEx function to check the operational state of the miniport adapter that represents a network interface card (NIC). |
| [NDIS_M_SEND_RESOURCES_HANDLER callback function](nc-ndis-ndis-m-send-resources-handler.md) | TBD |
| [MINIPORT_MESSAGE_INTERRUPT callback](nc-ndis-miniport-message-interrupt.md) | NDIS calls the MiniportMessageInterrupt function when a NIC generates a message-based interrupt. |
| [FILTER_NET_PNP_EVENT callback](nc-ndis-filter-net-pnp-event.md) | NDIS calls a filter driver's FilterNetPnPEvent function to notify the driver of network Plug and Play (PnP) and Power Management events.Note  You must declare the function by using the FILTER_NET_PNP_EVENT type. |
| [PROTOCOL_CM_DEACTIVATE_VC_COMPLETE callback](nc-ndis-protocol-cm-deactivate-vc-complete.md) | The ProtocolCmDeactivateVcComplete function is a required function. |
| [W_HANDLE_INTERRUPT_HANDLER callback function](nc-ndis-w-handle-interrupt-handler.md) | TBD |
| [ADAPTER_SHUTDOWN_HANDLER callback function](nc-ndis-adapter-shutdown-handler.md) | TBD |
| [W_TRANSFER_DATA_HANDLER callback function](nc-ndis-w-transfer-data-handler.md) | TBD |
| [MINIPORT_RESET callback](nc-ndis-miniport-reset.md) | NDIS calls an NDIS miniport driver's MiniportResetEx function to initiate a reset of a network interface card (NIC). For more information, see Miniport Adapter Check-for-Hang and Reset Operations and Miniport Driver Hardware Reset. |
| [W_CHECK_FOR_HANG_HANDLER callback function](nc-ndis-w-check-for-hang-handler.md) | TBD |
| [NDIS_WM_SEND_COMPLETE_HANDLER callback function](nc-ndis-ndis-wm-send-complete-handler.md) | TBD |
| [NDIS_M_TD_COMPLETE_HANDLER callback function](nc-ndis-ndis-m-td-complete-handler.md) | TBD |
| [PROTOCOL_CL_INCOMING_CALL_QOS_CHANGE callback](nc-ndis-protocol-cl-incoming-call-qos-change.md) | The ProtocolClIncomingCallQoSChange function is used by connection-oriented clients on networks that support dynamic quality-of-service. |
| [ETH_RCV_COMPLETE_HANDLER callback function](nc-ndis-eth-rcv-complete-handler.md) | TBD |
| [NDIS_PROCESS_SG_LIST callback](nc-ndis-ndis-process-sg-list.md) | The NetProcessSGList function (NDIS_PROCESS_SG_LIST_HANDLER entry point) processes a scatter/gather list. |
| [FILTER_DIRECT_OID_REQUEST_COMPLETE callback](nc-ndis-filter-direct-oid-request-complete.md) | NDIS calls the FilterDirectOidRequestComplete function to complete a filter driver direct OID request that queried or set information in an underlying driver.Note  You must declare the function by using the FILTER_DIRECT_OID_REQUEST_COMPLETE type. |
| [MINIPORT_SEND_NET_BUFFER_LISTS callback](nc-ndis-miniport-send-net-buffer-lists.md) | NDIS calls the MiniportSendNetBufferLists function to transmit network data that is contained in a linked list of NET_BUFFER_LIST structures. |
| [MINIPORT_CANCEL_IDLE_NOTIFICATION callback](nc-ndis-miniport-cancel-idle-notification.md) | NDIS calls the MiniportCancelIdleNotification handler function to notify the miniport driver that NDIS has detected activity on the suspended network adapter. |
| [W_RETURN_PACKET_HANDLER callback function](nc-ndis-w-return-packet-handler.md) | TBD |
| [CO_SEND_COMPLETE_HANDLER callback function](nc-ndis-co-send-complete-handler.md) | TBD |
| [PROTOCOL_CL_INCOMING_CLOSE_CALL callback](nc-ndis-protocol-cl-incoming-close-call.md) | The ProtocolClIncomingCloseCall function is used by all connection-oriented NDIS clients. |
| [WAN_SEND_COMPLETE_HANDLER callback function](nc-ndis-wan-send-complete-handler.md) | TBD |
| [PROTOCOL_CO_AF_REGISTER_NOTIFY callback](nc-ndis-protocol-co-af-register-notify.md) | The ProtocolCoAfRegisterNotify function is used by connection-oriented NDIS clients. |
| [REQUEST_HANDLER callback function](nc-ndis-request-handler.md) | TBD |
| [NDIS_SWITCH_GET_NET_BUFFER_LIST_SWITCH_CONTEXT callback](nc-ndis-ndis-switch-get-net-buffer-list-switch-context.md) | The Hyper-V extensible switch extension calls the GetNetBufferListSwitchContext function to retrieve the switch context previously set on the NET_BUFFER_LIST. |
| [TR_RCV_INDICATE_HANDLER callback function](nc-ndis-tr-rcv-indicate-handler.md) | TBD |
| [FILTER_CANCEL_DIRECT_OID_REQUEST callback](nc-ndis-filter-cancel-direct-oid-request.md) | NDIS calls a filter driver's FilterCancelDirectOidRequest function to cancel a direct OID request.Note  You must declare the function by using the FILTER_CANCEL_DIRECT_OID_REQUEST type. |
| [W_ALLOCATE_COMPLETE_HANDLER callback function](nc-ndis-w-allocate-complete-handler.md) | TBD |
| [NDIS_PD_ACQUIRE_RECEIVE_QUEUES callback function](nc-ndis-ndis-pd-acquire-receive-queues.md) | TBD |
| [PROTOCOL_UNBIND_ADAPTER_EX callback](nc-ndis-protocol-unbind-adapter-ex.md) | NDIS calls a protocol driver's ProtocolUnbindAdapterEx function to request the driver to unbind from an underlying miniport adapter.Note  You must declare the function by using the PROTOCOL_UNBIND_ADAPTER_EX type. |
| [MINIPORT_CANCEL_OID_REQUEST callback](nc-ndis-miniport-cancel-oid-request.md) | NDIS calls a miniport driver's MiniportCancelOidRequest function to cancel an OID request. |
| [PROTOCOL_CO_SEND_NET_BUFFER_LISTS_COMPLETE callback](nc-ndis-protocol-co-send-net-buffer-lists-complete.md) | The ProtocolCoSendNetBufferListsComplete function completes a send operation that the protocol driver initiated with a call to the NdisCoSendNetBufferLists function.Note  You must declare the function by using the PROTOCOL_CO_SEND_NET_BUFFER_LISTS_COMPLETE type. For more information, see the following Examples section. |
| [PROTOCOL_CL_DROP_PARTY_COMPLETE callback](nc-ndis-protocol-cl-drop-party-complete.md) | The ProtocolClDropPartyComplete function is used by connection-oriented NDIS clients that set up multipoint connections. |
| [MINIPORT_PAUSE callback](nc-ndis-miniport-pause.md) | NDIS calls a miniport driver's MiniportPause function to stop the flow of network data through a specified miniport adapter. |
| [FILTER_CANCEL_SEND_NET_BUFFER_LISTS callback function](nc-ndis-filter-cancel-send-net-buffer-lists.md) | TBD |
| [MINIPORT_SHUTDOWN callback](nc-ndis-miniport-shutdown.md) | NDIS calls a miniport driver's MiniportShutdownEx function when the system is shutting down. |
| [NDIS_SWITCH_ALLOCATE_NET_BUFFER_LIST_FORWARDING_CONTEXT callback](nc-ndis-ndis-switch-allocate-net-buffer-list-forwarding-context.md) | The AllocateNetBufferListForwardingContext function prepares a NET_BUFFER_LIST structure for send or receive operations within the extensible switch. |
| [PROTOCOL_CM_CLOSE_CALL callback](nc-ndis-protocol-cm-close-call.md) | The ProtocolCmCloseCall function is a required function that terminates an existing call and releases any resources that the call manager allocated for the call.Note  You must declare the function by using the PROTOCOL_CM_CLOSE_CALL type. |
| [CO_STATUS_HANDLER callback function](nc-ndis-co-status-handler.md) | TBD |
| [MINIPORT_REMOVE_DEVICE callback](nc-ndis-miniport-remove-device.md) | The MiniportRemoveDevice function releases resources that the MiniportAddDevice function allocated. |
| [RECEIVE_PACKET_HANDLER callback function](nc-ndis-receive-packet-handler.md) | TBD |
| [PROTOCOL_CO_OID_REQUEST_COMPLETE callback](nc-ndis-protocol-co-oid-request-complete.md) | The ProtocolCoOidRequestComplete function completes the processing of an asynchronous CoNDIS OID request.Note  You must declare the function by using the PROTOCOL_CO_OID_REQUEST_COMPLETE type. |
| [TRANSFER_DATA_HANDLER callback function](nc-ndis-transfer-data-handler.md) | TBD |
| [PROTOCOL_UNINSTALL callback](nc-ndis-protocol-uninstall.md) | NDIS calls a protocol driver's ProtocolUninstall function to perform cleanup operations before a protocol driver is uninstalled.Note  You must declare the function by using the PROTOCOL_UNINSTALL type. |
| [TDI_REGISTER_CALLBACK callback function](nc-ndis-tdi-register-callback.md) | TBD |
| [MINIPORT_CO_ACTIVATE_VC callback](nc-ndis-miniport-co-activate-vc.md) | The MiniportCoActivateVc function is required for connection-oriented miniports. |
| [NDIS_SWITCH_REPORT_FILTERED_NET_BUFFER_LISTS callback](nc-ndis-ndis-switch-report-filtered-net-buffer-lists.md) | The ReportFilteredNetBufferLists function reports on one or more network packets that were dropped or excluded from port delivery by the extensible switch extension. Each network packet is defined through a NET_BUFFER_LIST structure. |
| [W_CO_SEND_PACKETS_HANDLER callback function](nc-ndis-w-co-send-packets-handler.md) | TBD |
| [WM_TRANSFER_DATA_HANDLER callback function](nc-ndis-wm-transfer-data-handler.md) | TBD |
| [W_SET_INFORMATION_HANDLER callback function](nc-ndis-w-set-information-handler.md) | TBD |
| [FILTER_DETACH callback](nc-ndis-filter-detach.md) | NDIS calls a filter driver's FilterDetach function to release all the resources that are associated with a filter module.Note  You must declare the function by using the FILTER_DETACH type. |
| [PROTOCOL_CL_OPEN_AF_COMPLETE_EX callback](nc-ndis-protocol-cl-open-af-complete-ex.md) | The ProtocolClOpenAfCompleteEx function completes the opening of an address family (AF) that was started when a CoNDIS client called the NdisClOpenAddressFamilyEx function.Note  You must declare the function by using the PROTOCOL_CL_OPEN_AF_COMPLETE_EX type. For more information, see the following Examples section. |
| [FILTER_OID_REQUEST_COMPLETE callback](nc-ndis-filter-oid-request-complete.md) | NDIS calls the FilterOidRequestComplete function to complete a filter driver request that queried or set information in an underlying driver.Note  You must declare the function by using the FILTER_OID_REQUEST_COMPLETE type. |
| [PROTOCOL_CL_INCOMING_DROP_PARTY callback](nc-ndis-protocol-cl-incoming-drop-party.md) | The ProtocolClIncomingDropParty function is used by connection-oriented NDIS clients that set up multipoint connections. |
| [PROTOCOL_OID_REQUEST_COMPLETE callback](nc-ndis-protocol-oid-request-complete.md) | The ProtocolOidRequestComplete function completes the processing of a protocol driver-initiated OID request for which the NdisOidRequest function returned NDIS_STATUS_PENDING.Note  You must declare the function by using the PROTOCOL_OID_REQUEST_COMPLETE type. For more information, see the following Examples section. |
| [NDIS_SWITCH_UPDATE_NET_BUFFER_LIST_DESTINATIONS callback](nc-ndis-ndis-switch-update-net-buffer-list-destinations.md) | The Hyper-V extensible switch extension calls the UpdateNetBufferListDestinations function to commit modifications that the extension made to a packet that contains multiple extensible switch destination ports. |
| [TR_RCV_COMPLETE_HANDLER callback function](nc-ndis-tr-rcv-complete-handler.md) | TBD |
| [PROTOCOL_CM_MAKE_CALL callback](nc-ndis-protocol-cm-make-call.md) | The ProtocolCmMakeCall function is a required function that sets up media specific parameters for a virtual connection (VC) and activates the virtual connection.Note  You must declare the function by using the PROTOCOL_CM_MAKE_CALL type. |
| [STATUS_COMPLETE_HANDLER callback function](nc-ndis-status-complete-handler.md) | TBD |
| [FILTER_RECEIVE_NET_BUFFER_LISTS callback](nc-ndis-filter-receive-net-buffer-lists.md) | NDIS calls the FilterReceiveNetBufferLists function to request a filter driver to process a receive indication.Note  You must declare the function by using the FILTER_RECEIVE_NET_BUFFER_LISTS type. |
| [BIND_HANDLER callback function](nc-ndis-bind-handler.md) | TBD |
| [MINIPORT_MESSAGE_INTERRUPT_DPC callback](nc-ndis-miniport-message-interrupt-dpc.md) | A miniport driver must provide a MiniportMessageInterruptDPC handler if the driver calls the NdisMRegisterInterruptEx function to register an interrupt. |
| [NDIS_M_STS_COMPLETE_HANDLER callback function](nc-ndis-ndis-m-sts-complete-handler.md) | TBD |
| [MINIPORT_DEVICE_PNP_EVENT_NOTIFY callback](nc-ndis-miniport-device-pnp-event-notify.md) | NDIS calls a miniport driver's MiniportDevicePnPEventNotify function to notify the driver of Plug and Play (PnP) events. |
| [NDIS_IO_WORKITEM_FUNCTION callback function](nc-ndis-ndis-io-workitem-function.md) | TBD |
| [PROTOCOL_RECEIVE_NET_BUFFER_LISTS callback](nc-ndis-protocol-receive-net-buffer-lists.md) | The ProtocolReceiveNetBufferLists function processes receive indications from underlying drivers.Note  You must declare the function by using the PROTOCOL_RECEIVE_NET_BUFFER_LISTS type. |
| [TDI_PNP_HANDLER callback function](nc-ndis-tdi-pnp-handler.md) | TBD |
| [FREE_SHARED_MEMORY_HANDLER callback](nc-ndis-free-shared-memory-handler.md) | The NetFreeSharedMemory function (FREE_SHARED_MEMORY_HANDLER entry point) is called by NDIS when a driver frees shared memory from a shared memory provider. |
| [PROTOCOL_CO_CREATE_VC callback](nc-ndis-protocol-co-create-vc.md) | The ProtocolCoCreateVc function is a required function that allocates resources necessary for a call manager or client to activate and maintain a virtual connection (VC).Note  You must declare the function by using the PROTOCOL_CO_CREATE_VC type. |
| [SEND_PACKETS_HANDLER callback function](nc-ndis-send-packets-handler.md) | TBD |
| [W_RESET_HANDLER callback function](nc-ndis-w-reset-handler.md) | TBD |
| [W_QUERY_INFORMATION_HANDLER callback function](nc-ndis-w-query-information-handler.md) | TBD |
| [NDIS_PD_FREE_QUEUE callback](nc-ndis-ndis-pd-free-queue.md) | The PacketDirect (PD) platform calls a PD-capable miniport driver's NdisPDFreeQueue function to free a queue. |
| [OPEN_ADAPTER_COMPLETE_HANDLER callback function](nc-ndis-open-adapter-complete-handler.md) | TBD |
| [NDIS_SWITCH_DEREFERENCE_SWITCH_NIC callback](nc-ndis-ndis-switch-dereference-switch-nic.md) | The DereferenceSwitchNic function decrements the Hyper-V extensible switch reference counter for a network adapter that is connected to an extensible switch port. The reference counter was incremented through a previous call to ReferenceSwitchNic. |
| [RECEIVE_COMPLETE_HANDLER callback function](nc-ndis-receive-complete-handler.md) | TBD |
| [PROTOCOL_CM_INCOMING_CALL_COMPLETE callback](nc-ndis-protocol-cm-incoming-call-complete.md) | The ProtocolCmIncomingCallComplete function is required. |
| [CO_RECEIVE_PACKET_HANDLER callback function](nc-ndis-co-receive-packet-handler.md) | TBD |
| [MINIPORT_INITIALIZE callback](nc-ndis-miniport-initialize.md) | NDIS calls a miniport driver's MiniportInitializeEx function to initialize a miniport adapter for network I/O operations. |
| [MINIPORT_ALLOCATE_SHARED_MEM_COMPLETE callback](nc-ndis-miniport-allocate-shared-mem-complete.md) | NDIS calls a miniport driver's MiniportSharedMemoryAllocateComplete function to complete a shared memory allocation request that the miniport driver started by calling the NdisMAllocateSharedMemoryAsyncEx function. |
| [NDIS_PD_ALLOCATE_COUNTER callback](nc-ndis-ndis-pd-allocate-counter.md) | The PacketDirect (PD) platform calls a PD-capable miniport driver's NdisPDAllocateCounter function to allocate a counter object. |
| [NDIS_SWITCH_DEREFERENCE_SWITCH_PORT callback](nc-ndis-ndis-switch-dereference-switch-port.md) | The DereferenceSwitchPort function decrements the Hyper-V extensible switch reference counter for an extensible switch port. The reference counter was incremented through a previous call to ReferenceSwitchPort. |
| [FILTER_DEVICE_PNP_EVENT_NOTIFY callback](nc-ndis-filter-device-pnp-event-notify.md) | NDIS calls a filter driver's FilterDevicePnPEventNotify function to notify the driver of device Plug and Play (PnP) and Power Management events.Note  You must declare the function by using the FILTER_DEVICE_PNP_EVENT_NOTIFY type. |
| [PROTOCOL_CM_OPEN_AF callback](nc-ndis-protocol-cm-open-af.md) | The ProtocolCmOpenAf function is required. |
| [MINIPORT_PNP_IRP callback function](nc-ndis-miniport-pnp-irp.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [NDIS_PROTOCOL_PAUSE_PARAMETERS structure](ns-ndis--ndis-protocol-pause-parameters.md) | NDIS passes an NDIS_PROTOCOL_PAUSE_PARAMETERS structure to a protocol driver when it calls the ProtocolNetPnPEvent function to indicate a NetEventPause event. |
| [NDIS_CALL_MANAGER_CHARACTERISTICS structure](ns-ndis--ndis-call-manager-characteristics~r1.md) | TBD |
| [NDIS_MINIPORT_ADAPTER_ATTRIBUTES structure](ns-ndis--ndis-miniport-adapter-attributes.md) | The NDIS_MINIPORT_ADAPTER_ATTRIBUTES structure is a placeholder for the following structures |
| [NDIS_PACKET_EXTENSION structure](ns-ndis--ndis-packet-extension.md) | TBD |
| [NET_BUFFER_LIST structure](ns-ndis--net-buffer-list.md) | TBD |
| [NDIS_PROTOCOL_RESTART_PARAMETERS structure](ns-ndis--ndis-protocol-restart-parameters.md) | The NDIS_PROTOCOL_RESTART_PARAMETERS structure defines restart parameters for a protocol driver when NDIS calls the ProtocolNetPnPEvent function to indicate a NetEventRestart event. |
| [NDIS51_MINIPORT_CHARACTERISTICS structure](ns-ndis--ndis51-miniport-characteristics~r1.md) | TBD |
| [NDIS_MINIPORT_PAUSE_PARAMETERS structure](ns-ndis--ndis-miniport-pause-parameters.md) | The NDIS_MINIPORT_PAUSE_PARAMETERS structure defines pause parameters for miniport adapters. |
| [VAR_STRING structure](ns-ndis--var-string.md) | TBD |
| [NDIS_NBL_MEDIA_MEDIA_SPECIFIC_INFORMATION structure](ns-ndis--ndis-nbl-media-media-specific-information~r1.md) | The NDIS_NBL_MEDIA_SPECIFIC_INFORMATION structure specifies media-specific data that is associated with a NET_BUFFER_LIST structure. |
| [IPSEC_OFFLOAD_V2_ADD_SA structure](ns-ndis--ipsec-offload-v2-add-sa.md) | TBD |
| [NDIS_OID_REQUEST structure](ns-ndis--ndis-oid-request.md) | To query or set OID information, NDIS submits NDIS_OID_REQUEST structures to filter drivers and miniport drivers. |
| [X_FILTER structure](ns-ndis--x-filter~r2.md) | TBD |
| [NDIS_RW_LOCK_EX structure](ns-ndis--ndis-rw-lock-ex~r1.md) | TBD |
| [NDIS_WORK_ITEM structure](ns-ndis--ndis-work-item.md) | TBD |
| [NDIS_PD_PROVIDER_DISPATCH structure](ns-ndis--ndis-pd-provider-dispatch.md) | This structure is used as input for the OID_PD_OPEN_PROVIDER and serves as a container for all the provider's driver routines. |
| [NDIS_PD_POST_AND_DRAIN_ARG structure](ns-ndis--ndis-pd-post-and-drain-arg.md) | TBD |
| [IPSEC_OFFLOAD_V2_DELETE_SA structure](ns-ndis--ipsec-offload-v2-delete-sa~r1.md) | The IPSEC_OFFLOAD_V2_DELETE_SA structure specifies a security association (SA) that should be deleted from a NIC and a pointer to the next IPSEC_OFFLOAD_V2_DELETE_SA structure in a linked list. |
| [NDIS_MINIPORT_ADAPTER_NDK_ATTRIBUTES structure](ns-ndis--ndis-miniport-adapter-ndk-attributes.md) | The NDIS_MINIPORT_ADAPTER_NDK_ATTRIBUTES structure specifies the NDK-capabilities of a miniport adapter. This structure is used in the NDKAttributes member of the NDIS_MINIPORT_ADAPTER_ATTRIBUTES union. |
| [NDIS_SWITCH_FORWARDING_DESTINATION_ARRAY structure](ns-ndis--ndis-switch-forwarding-destination-array.md) | TBD |
| [NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS structure](ns-ndis--ndis-co-call-manager-optional-handlers.md) | The NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS structure specifies CoNDIS call manager ProtocolXxx functions for the driver that passes this structure to the NdisSetOptionalHandlers function. |
| [NDIS_SPIN_LOCK structure](ns-ndis--ndis-spin-lock.md) | TBD |
| [NDIS_TASK_TCP_LARGE_SEND structure](ns-ndis--ndis-task-tcp-large-send.md) | TBD |
| [NET_PNP_EVENT_NOTIFICATION structure](ns-ndis--net-pnp-event-notification.md) | The NET_PNP_EVENT_NOTIFICATION structure describes a network Plug and Play (PnP) event, an NDIS PnP event, or a power management event. |
| [NDIS_DEVICE_OBJECT_ATTRIBUTES structure](ns-ndis--ndis-device-object-attributes.md) | The NDIS_DEVICE_OBJECT_ATTRIBUTES structure defines the attributes of a device that an NDIS filter or miniport driver can pass to the NdisRegisterDeviceEx function. |
| [NET_BUFFER_DATA_LENGTH structure](ns-ndis--net-buffer-data-length.md) | TBD |
| [NDIS_NET_BUFFER_LIST_VIRTUAL_SUBNET_INFO structure](ns-ndis--ndis-net-buffer-list-virtual-subnet-info.md) | Defines the group network virtualization information for a network buffer list (NBL). |
| [NDIS_TASK_IPSEC structure](ns-ndis--ndis-task-ipsec.md) | TBD |
| [NET_BUFFER_POOL_PARAMETERS structure](ns-ndis--net-buffer-pool-parameters.md) | TBD |
| [NDIS_PD_QUEUE structure](ns-ndis--ndis-pd-queue.md) | TBD |
| [NDIS_RECEIVE_QUEUE_STATE structure](ns-ndis--ndis-receive-queue-state.md) | The NDIS_RECEIVE_QUEUE_STATE structure contains information about the operational state of a receive queue. |
| [NET_PNP_EVENT structure](ns-ndis--net-pnp-event.md) | The NET_PNP_EVENT structure describes a network Plug and Play (PnP) event, an NDIS PnP event, or a power management event. |
| [LOCK_STATE structure](ns-ndis--lock-state.md) | The LOCK_STATE structure tracks the state of a read/write lock. |
| [PD_BUFFER structure](ns-ndis--pd-buffer.md) | This structure represents a PacketDirect (PD) packet, or a portion of a PD packet in a queue. |
| [NDIS_MINIPORT_INTERRUPT_CHARACTERISTICS structure](ns-ndis--ndis-miniport-interrupt-characteristics.md) | An NDIS miniport driver defines its interrupt characteristics in an NDIS_MINIPORT_INTERRUPT_CHARACTERISTICS structure and passes the structure to the NdisMRegisterInterruptEx function. |
| [CO_ADDRESS structure](ns-ndis--co-address.md) | TBD |
| [X_FILTER structure](ns-ndis--x-filter.md) | TBD |
| [NDIS_MSIX_CONFIG_PARAMETERS structure](ns-ndis--ndis-msix-config-parameters.md) | The NDIS_MSIX_CONFIG_PARAMETERS structure defines a requested configuration operation and specifies the parameters that are required for that particular operation. |
| [NDIS_GENERIC_OBJECT structure](ns-ndis--ndis-generic-object.md) | The NDIS_GENERIC_OBJECT structure defines a generic object which a software component can use to obtain an NDIS handle. |
| [NDIS_RW_LOCK_REFCOUNT structure](ns-ndis--ndis-rw-lock-refcount.md) | The NDIS_RW_LOCK_REFCOUNT union defines attributes of a read/write lock. |
| [NDIS_IF_PROVIDER_CHARACTERISTICS structure](ns-ndis--ndis-if-provider-characteristics.md) | The NDIS_IF_PROVIDER_CHARACTERISTICS structure defines NDIS network interface provider entry points and other provider characteristics. |
| [PD_BUFFER_8021Q_INFO structure](ns-ndis--pd-buffer-8021q-info.md) | This structure contains the IEEE 802.1Q information. |
| [NET_BUFFER_LIST_HEADER structure](ns-ndis--net-buffer-list-header.md) | The NET_BUFFER_LIST_HEADER defines header information for the NET_BUFFER_LIST structure. |
| [SCATTER_GATHER_LIST structure](ns-ndis--scatter-gather-list~r1.md) | TBD |
| [NDIS_MINIPORT_ADAPTER_HARDWARE_ASSIST_ATTRIBUTES structure](ns-ndis--ndis-miniport-adapter-hardware-assist-attributes.md) | The NDIS_MINIPORT_ADAPTER_HARDWARE_ASSIST_ATTRIBUTES structure specifies the hardware-assisted attributes of the network adapter. |
| [NDIS_RW_LOCK_EX structure](ns-ndis--ndis-rw-lock-ex.md) | TBD |
| [IPSEC_OFFLOAD_V2_ADD_SA_EX structure](ns-ndis--ipsec-offload-v2-add-sa-ex.md) | TBD |
| [NET_BUFFER_LIST_DATA structure](ns-ndis--net-buffer-list-data.md) | The NET_BUFFER_LIST_DATA structure contains management data for the NET_BUFFER structures that are linked to a NET_BUFFER_LIST structure. |
| [NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO structure](ns-ndis--ndis-ipsec-offload-v2-header-net-buffer-list-info.md) | The NDIS_IPSEC_OFFLOAD_V2_HEADER_NET_BUFFER_LIST_INFO structure specifies IPsec header information in the OOB data of a NET_BUFFER_LIST structure. |
| [NDIS30_MINIPORT_CHARACTERISTICS structure](ns-ndis--ndis30-miniport-characteristics.md) | TBD |
| [PFILTERDBS structure](ns-ndis-pfilterdbs.md) | TBD |
| [NDIS_RSC_NBL_INFO structure](ns-ndis--ndis-rsc-nbl-info.md) | The NDIS_RSC_NBL_INFO union specifies receive segment coalescing (RSC) counter information that is associated with a NET_BUFFER_LIST structure. |
| [NDIS_FILTER_RESTART_PARAMETERS structure](ns-ndis--ndis-filter-restart-parameters.md) | The NDIS_FILTER_RESTART_PARAMETERS structure defines the restart parameters for the filter module. |
| [CO_PVC structure](ns-ndis--co-pvc.md) | TBD |
| [NDIS_OFFLOAD_ENCAPSULATION structure](ns-ndis--ndis-offload-encapsulation.md) | The NDIS_OFFLOAD_ENCAPSULATION structure specifies encapsulation settings when it is used with the OID_OFFLOAD_ENCAPSULATION OID. |
| [NDIS_PD_COUNTER_PARAMETERS structure](ns-ndis--ndis-pd-counter-parameters.md) | This structure holds parameters for the provider counter. |
| [NDIS_FILTER_PARTIAL_CHARACTERISTICS structure](ns-ndis--ndis-filter-partial-characteristics.md) | To specify optional entry points for a filter module, a filter driver initializes an NDIS_FILTER_PARTIAL_CHARACTERISTICS structure and passes it to the NdisSetOptionalHandlers function. |
| [NDIS_MINIPORT_TIMER structure](ns-ndis--ndis-miniport-timer.md) | TBD |
| [NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO structure](ns-ndis--ndis-switch-forwarding-detail-net-buffer-list-info.md) | The NDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO union specifies the information for forwarding a packet to one or more Hyper-V extensible switch ports. |
| [NDIS_PROTOCOL_DRIVER_CHARACTERISTICS structure](ns-ndis--ndis-protocol-driver-characteristics.md) | To specify its driver characteristics, a protocol driver initializes an NDIS_PROTOCOL_DRIVER_CHARACTERISTICS structure and passes it to NDIS. |
| [NDIS_MINIPORT_DRIVER_CHARACTERISTICS structure](ns-ndis--ndis-miniport-driver-characteristics.md) | An NDIS driver initializes an NDIS_MINIPORT_DRIVER_CHARACTERISTICS structure to define its miniport driver characteristics, including the entry points for its MiniportXxx functions. |
| [NDIS40_PROTOCOL_CHARACTERISTICS structure](ns-ndis--ndis40-protocol-characteristics.md) | TBD |
| [NDIS_PD_COUNTER_VALUE structure](ns-ndis--ndis-pd-counter-value.md) | This structure is used to hold a counter value for a queue or filter counter. |
| [NDIS_SCATTER_GATHER_LIST_PARAMETERS structure](ns-ndis--ndis-scatter-gather-list-parameters.md) | The NDIS_SCATTER_GATHER_LIST_PARAMETERS structure specifies parameters that NDIS uses to build a scatter/gather list for a buffer. |
| [CO_MEDIA_PARAMETERS structure](ns-ndis--co-media-parameters~r2.md) | TBD |
| [NDIS_OPEN_PARAMETERS structure](ns-ndis--ndis-open-parameters.md) | The NDIS_OPEN_PARAMETERS structure defines the open parameters when a protocol driver calls the NdisOpenAdapterEx function. |
| [CO_CALL_PARAMETERS structure](ns-ndis--co-call-parameters.md) | TBD |
| [CO_CALL_PARAMETERS structure](ns-ndis--co-call-parameters~r2.md) | TBD |
| [NDIS_TIMER_CHARACTERISTICS structure](ns-ndis--ndis-timer-characteristics.md) | The NDIS_TIMER_CHARACTERISTICS structure defines characteristics of a one-shot or periodic timer. |
| [LOCK_STATE_EX structure](ns-ndis--lock-state-ex.md) | The LOCK_STATE_EX structure tracks the state of a read/write lock. |
| [NDIS_SWITCH_NIC_STATUS_INDICATION structure](ns-ndis--ndis-switch-nic-status-indication.md) | The NDIS_SWITCH_NIC_STATUS_INDICATION structure specifies the information that is required to forward or originate an NDIS status indication from an underlying physical network adapter. |
| [NDIS_DMA_BLOCK structure](ns-ndis--ndis-dma-block.md) | TBD |
| [NDIS_AF_LIST structure](ns-ndis--ndis-af-list.md) | TBD |
| [NDIS_IPSEC_OFFLOAD_V2_TUNNEL_NET_BUFFER_LIST_INFO structure](ns-ndis--ndis-ipsec-offload-v2-tunnel-net-buffer-list-info.md) | The NDIS_IPSEC_OFFLOAD_V2_TUNNEL_NET_BUFFER_LIST_INFO structure specifies the security association (SA) offload handle to the tunnel portion of a send packet. |
| [NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO structure](ns-ndis--ndis-tcp-ip-checksum-net-buffer-list-info.md) | The NDIS_TCP_IP_CHECKSUM_NET_BUFFER_LIST_INFO structure specifies information used in offloading checksum tasks from the TCP/IP transport to a NIC. |
| [NDIS_CO_CLIENT_OPTIONAL_HANDLERS structure](ns-ndis--ndis-co-client-optional-handlers.md) | The NDIS_CO_CLIENT_OPTIONAL_HANDLERS structure specifies entry points for CoNDIS client ProtocolXxx functions for the protocol driver that passes this structure to the NdisSetOptionalHandlers function. |
| [NDIS_TASK_OFFLOAD_HEADER structure](ns-ndis--ndis-task-offload-header.md) | TBD |
| [NDIS_WRAPPER_HANDLE structure](ns-ndis--ndis-wrapper-handle.md) | TBD |
| [NDIS_OFFLOAD structure](ns-ndis--ndis-offload.md) | TBD |
| [NDIS_PACKET_PRIVATE structure](ns-ndis--ndis-packet-private.md) | TBD |
| [PD_BUFFER_VIRTUAL_SUBNET_INFO structure](ns-ndis--pd-buffer-virtual-subnet-info.md) | This structure contains the virtual subnet information. |
| [NDIS_SHARED_MEMORY_PARAMETERS structure](ns-ndis--ndis-shared-memory-parameters.md) | The NDIS_SHARED_MEMORY_PARAMETERS structure specifies the shared memory parameters for a shared memory allocation request. |
| [NDIS_PACKET structure](ns-ndis--ndis-packet~r1.md) | TBD |
| [NDIS_MINIPORT_ADAPTER_OFFLOAD_ATTRIBUTES structure](ns-ndis--ndis-miniport-adapter-offload-attributes.md) | An NDIS miniport driver sets up an NDIS_MINIPORT_ADAPTER_OFFLOAD_ATTRIBUTES structure to define task offload and connection offload attributes, if any, that are associated with a miniport adapter. |
| [IPSEC_OFFLOAD_V2_SECURITY_ASSOCIATION structure](ns-ndis--ipsec-offload-v2-security-association.md) | The IPSEC_OFFLOAD_V2_SECURITY_ASSOCIATION structure specifies a single security association (SA). |
| [NDIS_RESTART_GENERAL_ATTRIBUTES structure](ns-ndis--ndis-restart-general-attributes.md) | The NDIS_RESTART_GENERAL_ATTRIBUTES structure defines the general restart attributes that are associated with a miniport adapter. |
| [NDIS_FILTER_PAUSE_PARAMETERS structure](ns-ndis--ndis-filter-pause-parameters.md) | The NDIS_FILTER_PAUSE_PARAMETERS structure defines the pause parameters for the filter module. |
| [NDIS_PD_FILTER_COUNTER structure](ns-ndis--ndis-pd-filter-counter.md) | This structure is used to hold counter information for a filter. |
| [NET_DEVICE_PNP_EVENT structure](ns-ndis--net-device-pnp-event.md) | The NET_DEVICE_PNP_EVENT structure defines device plug and play (PnP) events for miniport adapters. |
| [NDIS_FILTER_DRIVER_CHARACTERISTICS structure](ns-ndis--ndis-filter-driver-characteristics.md) | To specify its driver characteristics, a filter driver initializes an NDIS_FILTER_DRIVER_CHARACTERISTICS structure and passes it to NDIS. |
| [NDIS_HD_SPLIT_ATTRIBUTES structure](ns-ndis--ndis-hd-split-attributes.md) | The NDIS_HD_SPLIT_ATTRIBUTES structure defines header-data split attributes, if any, that are associated with a miniport adapter. |
| [NDIS_WAN_GET_STATS structure](ns-ndis--ndis-wan-get-stats.md) | TBD |
| [NDIS_COMMON_OPEN_BLOCK structure](ns-ndis--ndis-common-open-block.md) | TBD |
| [NDIS_REQUEST structure](ns-ndis--ndis-request.md) | TBD |
| [NDIS_SG_DMA_DESCRIPTION structure](ns-ndis--ndis-sg-dma-description.md) | TBD |
| [NDIS_FILTER_INTERFACE structure](ns-ndis--ndis-filter-interface.md) | The NDIS_FILTER_INTERFACE structure defines the attributes for an NDIS filter. |
| [NDIS_TASK_OFFLOAD structure](ns-ndis--ndis-task-offload.md) | TBD |
| [NET_BUFFER_LIST_CONTEXT structure](ns-ndis--net-buffer-list-context~r1.md) | The NET_BUFFER_LIST_CONTEXT structure stores context information for a NET_BUFFER_LIST structure. |
| [IPSEC_OFFLOAD_V2_ADD_SA_EX structure](ns-ndis--ipsec-offload-v2-add-sa-ex~r1.md) | The IPSEC_OFFLOAD_V2_ADD_SA_EX structure defines information about a security association (SA) that a miniport driver should add to a NIC. |
| [NDIS_MINIPORT_BLOCK structure](ns-ndis--ndis-miniport-block.md) | TBD |
| [NDIS_FILTER_ATTACH_PARAMETERS structure](ns-ndis--ndis-filter-attach-parameters.md) | The NDIS_FILTER_ATTACH_PARAMETERS structure defines the initialization parameters for the filter module. |
| [NDIS_NET_BUFFER_LIST_8021Q_INFO structure](ns-ndis--ndis-net-buffer-list-8021q-info.md) | The NDIS_NET_BUFFER_LIST_8021Q_INFO structure specifies 802.1Q information that is associated with a NET_BUFFER_LIST structure. |
| [NDIS_RW_LOCK_EX structure](ns-ndis--ndis-rw-lock-ex~r2.md) | TBD |
| [NDIS_BIND_FAILED_NOTIFICATION structure](ns-ndis--ndis-bind-failed-notification.md) | The NDIS_BIND_FAILED_NOTIFICATION structure describes a binding event failure. |
| [REFERENCE structure](ns-ndis--reference.md) | TBD |
| [NDIS_SWITCH_NET_BUFFER_LIST_CONTEXT_TYPE_INFO structure](ns-ndis--ndis-switch-net-buffer-list-context-type-info.md) | TBD |
| [NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO structure](ns-ndis--ndis-tcp-large-send-offload-net-buffer-list-info.md) | The NDIS_TCP_LARGE_SEND_OFFLOAD_NET_BUFFER_LIST_INFO structure specifies information that is used in offloading large send offload (LSO) tasks from the TCP/IP transport to a miniport adapter. |
| [NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES structure](ns-ndis--ndis-miniport-adapter-general-attributes.md) | An NDIS miniport driver sets up an NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES structure to define the general miniport driver attributes that are associated with a miniport adapter. |
| [NDIS_ENUM_FILTERS structure](ns-ndis--ndis-enum-filters.md) | The NDIS_ENUM_FILTERS structure is returned from the call to the NdisEnumerateFilterModules function to provide filter information for a filter stack. |
| [NDIS_NET_BUFFER_LIST_GFT_OFFLOAD_INFO structure](ns-ndis--ndis-net-buffer-list-gft-offload-info.md) | TBD |
| [IPSEC_OFFLOAD_V2_UPDATE_SA structure](ns-ndis--ipsec-offload-v2-update-sa.md) | The IPSEC_OFFLOAD_V2_UPDATE_SA structure updates information about security associations (SAs) that a miniport driver previously added to a NIC and a pointer to the next IPSEC_OFFLOAD_V2_UPDATE_SA structure in a linked list. |
| [NDIS_MINIPORT_INIT_PARAMETERS structure](ns-ndis--ndis-miniport-init-parameters.md) | The NDIS_MINIPORT_INIT_PARAMETERS structure defines the initialization parameters for a miniport adapter. |
| [NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO structure](ns-ndis--ndis-tcp-send-offloads-supplemental-net-buffer-list-info.md) | The NDIS_TCP_SEND_OFFLOADS_SUPPLEMENTAL_NET_BUFFER_LIST_INFO structure contains additional out-of-band information for encapsulated packets. |
| [NET_BUFFER_SHARED_MEMORY structure](ns-ndis--net-buffer-shared-memory~r1.md) | The NET_BUFFER_SHARED_MEMORY structure specifies a shared memory buffer that is associated with a NET_BUFFER structure. |
| [NDIS_MINIPORT_ADAPTER_PACKET_DIRECT_ATTRIBUTES structure](ns-ndis--ndis-miniport-adapter-packet-direct-attributes.md) | TBD |
| [SCATTER_GATHER_LIST structure](ns-ndis--scatter-gather-list.md) | TBD |
| [NDIS_BIND_PARAMETERS structure](ns-ndis--ndis-bind-parameters.md) | NDIS initializes an NDIS_BIND_PARAMETERS structure with information that defines the characteristics of a binding and passes it to a protocol driver. |
| [NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES structure](ns-ndis--ndis-miniport-adapter-registration-attributes.md) | An NDIS miniport driver sets up an NDIS_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES structure to define registration attributes that are associated with a miniport adapter. |
| [CO_MEDIA_PARAMETERS structure](ns-ndis--co-media-parameters.md) | TBD |
| [NDIS_CALL_MANAGER_CHARACTERISTICS structure](ns-ndis--ndis-call-manager-characteristics.md) | TBD |
| [NDIS_MINIPORT_SS_CHARACTERISTICS structure](ns-ndis--ndis-miniport-ss-characteristics.md) | The NDIS_MINIPORT_SS_CHARACTERISTICS structure specifies the pointers to a miniport driver's NDIS selective suspend handler functions. These functions are called by NDIS to issue idle notifications to the driver during a selective suspend operation. |
| [NDIS51_MINIPORT_CHARACTERISTICS structure](ns-ndis--ndis51-miniport-characteristics.md) | TBD |
| [NDIS_WAN_FRAGMENT structure](ns-ndis--ndis-wan-fragment.md) | TBD |
| [NDIS_NET_BUFFER_LIST_FILTERING_INFO structure](ns-ndis--ndis-net-buffer-list-filtering-info.md) | The NDIS_NET_BUFFER_LIST_FILTERING_INFO structure defines filtering information that is associated with a NET_BUFFER_LIST structure. |
| [NDIS_NET_BUFFER_LIST_MEDIA_SPECIFIC_INFO structure](ns-ndis--ndis-net-buffer-list-media-specific-info.md) | TBD |
| [NDIS_PD_TRANSMIT_QUEUE_COUNTER structure](ns-ndis--ndis-pd-transmit-queue-counter.md) | This structure is used to hold counter information for a transmit queue. |
| [CO_MEDIA_PARAMETERS structure](ns-ndis--co-media-parameters~r1.md) | TBD |
| [IPSEC_OFFLOAD_V2_ADD_SA structure](ns-ndis--ipsec-offload-v2-add-sa~r1.md) | The IPSEC_OFFLOAD_V2_ADD_SA structure defines information about a security association (SA) that a miniport driver should add to a NIC. |
| [NET_BUFFER_DATA structure](ns-ndis--net-buffer-data.md) | The NET_BUFFER_DATA structure contains information for managing the data buffers that are attached to a NET_BUFFER structure, and it identifies the next NET_BUFFER structure in a list of NET_BUFFER structures. |
| [NDIS_ENCAPSULATION_FORMAT structure](ns-ndis--ndis-encapsulation-format.md) | TBD |
| [NDIS_PD_QUEUE structure](ns-ndis--ndis-pd-queue~r1.md) | This structure represents a provider's receive or transmit queue. |
| [NDIS_SWITCH_OPTIONAL_HANDLERS structure](ns-ndis--ndis-switch-optional-handlers.md) | The NDIS_SWITCH_OPTIONAL_HANDLERS structure specifies the pointers to the Hyper-V extensible switch handler functions. These functions can be called by an extensible switch extension. |
| [NDIS_WAN_PACKET structure](ns-ndis--ndis-wan-packet.md) | TBD |
| [NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO structure](ns-ndis--ndis-ipsec-offload-v2-net-buffer-list-info.md) | The NDIS_IPSEC_OFFLOAD_V2_NET_BUFFER_LIST_INFO structure specifies information that is used in offloading Internet protocol security offload version 2 (IPsecOV2) tasks from the TCP/IP transport to a NIC. |
| [NDIS_DRIVER_OPTIONAL_HANDLERS structure](ns-ndis--ndis-driver-optional-handlers.md) | TBD |
| [NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS structure](ns-ndis--ndis-shared-memory-provider-characteristics.md) | The NDIS_SHARED_MEMORY_PROVIDER_CHARACTERISTICS structure specifies shared memory provider characteristics. |
| [PCO_ADDRESS_FAMILY structure](ns-ndis-pco-address-family.md) | TBD |
| [NDIS_MINIPORT_CO_CHARACTERISTICS structure](ns-ndis--ndis-miniport-co-characteristics.md) | The NDIS_MINIPORT_CO_CHARACTERISTICS structure specifies the CoNDIS entry points for a CoNDIS miniport driver. |
| [IPSEC_OFFLOAD_V2_DELETE_SA structure](ns-ndis--ipsec-offload-v2-delete-sa.md) | TBD |
| [NDIS_PACKET_8021Q_INFO structure](ns-ndis--ndis-packet-8021q-info.md) | TBD |
| [NET_BUFFER_LIST_POOL_PARAMETERS structure](ns-ndis--net-buffer-list-pool-parameters.md) | The NET_BUFFER_LIST_POOL_PARAMETERS structure defines the parameters for a pool of NET_BUFFER_LIST structures. |
| [NDIS_DMA_DESCRIPTION structure](ns-ndis--ndis-dma-description.md) | TBD |
| [NDIS_MINIPORT_PNP_CHARACTERISTICS structure](ns-ndis--ndis-miniport-pnp-characteristics.md) | The NDIS_MINIPORT_PNP_CHARACTERISTICS structure specifies entry points for functions that allow a miniport driver to process some Plug and Play (PnP) I/O request packets (IRPs). |
| [NDIS_PACKET_OOB_DATA structure](ns-ndis--ndis-packet-oob-data.md) | TBD |
| [NDIS_IPSEC_OFFLOAD_V1_NET_BUFFER_LIST_INFO structure](ns-ndis--ndis-ipsec-offload-v1-net-buffer-list-info.md) | The NDIS_IPSEC_OFFLOAD_V1_NET_BUFFER_LIST_INFO structure specifies information that is used in offloading Internet protocol security (IPsec) tasks from the TCP/IP transport to a miniport driver. |
| [NDIS50_MINIPORT_CHARACTERISTICS structure](ns-ndis--ndis50-miniport-characteristics~r1.md) | TBD |
| [NDIS_SYSTEM_PROCESSOR_INFO structure](ns-ndis--ndis-system-processor-info.md) | The NDIS_SYSTEM_PROCESSOR_INFO structure specifies information about the CPU topology of the local computer and the receive side scaling (RSS) processor set. |
| [NDIS_OPEN_BLOCK structure](ns-ndis--ndis-open-block.md) | TBD |
| [NDIS_NBL_MEDIA_MEDIA_SPECIFIC_INFORMATION structure](ns-ndis--ndis-nbl-media-media-specific-information.md) | The NDIS_NBL_MEDIA_SPECIFIC_INFORMATION structure specifies media-specific data that is associated with a NET_BUFFER_LIST structure. |
| [NDIS_OPEN_BLOCK structure](ns-ndis--ndis-open-block~r1.md) | TBD |
| [NET_BUFFER_LIST_CONTEXT structure](ns-ndis--net-buffer-list-context.md) | TBD |
| [NDIS_RECEIVE_THROTTLE_PARAMETERS structure](ns-ndis--ndis-receive-throttle-parameters.md) | The NDIS_RECEIVE_THROTTLE_PARAMETERS structure specifies the maximum number of NET_BUFFER_LIST structures that a miniport driver should indicate in a deferred procedure call (DPC). |
| [NDIS_MINIPORT_BLOCK structure](ns-ndis--ndis-miniport-block~r1.md) | TBD |
| [NDIS_PROTOCOL_BLOCK structure](ns-ndis--ndis-protocol-block.md) | TBD |
| [NDIS_PROCESSOR_INFO structure](ns-ndis--ndis-processor-info.md) | The NDIS_PROCESSOR_INFO structure specifies information about a processor in the local computer. |
| [NDIS_RESTART_ATTRIBUTES structure](ns-ndis--ndis-restart-attributes~r1.md) | The NDIS_RESTART_ATTRIBUTES structure identifies an attributes entry in a linked list of restart attributes. |
| [NDIS_RECEIVE_FILTER_QUEUE_STATE_CHANGE structure](ns-ndis--ndis-receive-filter-queue-state-change.md) | TBD |
| [NDIS_PHYSICAL_ADDRESS_UNIT structure](ns-ndis--ndis-physical-address-unit.md) | TBD |
| [NDIS_MINIPORT_ADAPTER_NATIVE_802_11_ATTRIBUTES structure](ns-ndis--ndis-miniport-adapter-native-802-11-attributes.md) | TBD |
| [NDIS_CONFIGURATION_OBJECT structure](ns-ndis--ndis-configuration-object.md) | The NDIS_CONFIGURATION_OBJECT structure defines the attributes of a configuration object that an NDIS driver can pass to the NdisOpenConfigurationEx function. |
| [NET_BUFFER_SHARED_MEMORY structure](ns-ndis--net-buffer-shared-memory.md) | TBD |
| [NDIS_WAN_LINE_DOWN structure](ns-ndis--ndis-wan-line-down.md) | TBD |
| [CO_ADDRESS_LIST structure](ns-ndis--co-address-list.md) | TBD |
| [NDIS_MINIPORT_INTERRUPT structure](ns-ndis--ndis-miniport-interrupt.md) | TBD |
| [NDIS_TCP_IP_CHECKSUM_PACKET_INFO structure](ns-ndis--ndis-tcp-ip-checksum-packet-info.md) | TBD |
| [X_FILTER structure](ns-ndis--x-filter~r1.md) | TBD |
| [NDIS_TASK_TCP_IP_CHECKSUM structure](ns-ndis--ndis-task-tcp-ip-checksum.md) | TBD |
| [NDIS_SWITCH_PORT_DESTINATION structure](ns-ndis--ndis-switch-port-destination.md) | The NDIS_SWITCH_PORT_DESTINATION structure specifies the Hyper-V extensible switch destination port to which a packet will be delivered. |
| [NDIS_TIMER structure](ns-ndis--ndis-timer.md) | TBD |
| [NDIS_WAN_LINE_UP structure](ns-ndis--ndis-wan-line-up.md) | TBD |
| [NET_IF_INFORMATION structure](ns-ndis--net-if-information.md) | The NET_IF_INFORMATION structure provides NDIS with information about a registered network interface. |
| [CO_CALL_PARAMETERS structure](ns-ndis--co-call-parameters~r1.md) | TBD |
| [NDIS_MINIPORT_RESTART_PARAMETERS structure](ns-ndis--ndis-miniport-restart-parameters.md) | The NDIS_MINIPORT_RESTART_PARAMETERS structure defines the restart parameters for a miniport adapter. |
| [PCO_SAP structure](ns-ndis-pco-sap.md) | TBD |
| [NDIS_RW_LOCK structure](ns-ndis--ndis-rw-lock.md) | The NDIS_RW_LOCK structure defines the attributes of a read/write lock. |
| [NDIS_M_DRIVER_BLOCK structure](ns-ndis--ndis-m-driver-block.md) | TBD |
| [NET_BUFFER_HEADER structure](ns-ndis--net-buffer-header.md) | The NET_BUFFER_HEADER structure specifies header information for the NET_BUFFER structure. |
| [BINARY_DATA structure](ns-ndis-binary-data.md) | The BINARY_DATA structure contains the binary data of a named entry in the registry. |
| [NDIS_SRIOV_VF_CONFIG_STATE structure](ns-ndis--ndis-sriov-vf-config-state.md) | TBD |
| [NDIS_STATUS_INDICATION structure](ns-ndis--ndis-status-indication.md) | NDIS and underlying drivers use the NDIS_STATUS_INDICATION structure to provide status indications to overlying protocol drivers. |
| [NDIS_RESTART_ATTRIBUTES structure](ns-ndis--ndis-restart-attributes.md) | TBD |
| [NDIS_WORK_ITEM structure](ns-ndis--ndis-work-item~r1.md) | TBD |
| [NDIS_DRIVER_WRAPPER_HANDLE structure](ns-ndis--ndis-driver-wrapper-handle.md) | TBD |
| [NDIS_CONFIGURATION_PARAMETER structure](ns-ndis--ndis-configuration-parameter.md) | The NDIS_CONFIGURATION_PARAMETER structure contains the data and type of a named entry in the registry. |
| [NDIS_MINIPORT_ADD_DEVICE_REGISTRATION_ATTRIBUTES structure](ns-ndis--ndis-miniport-add-device-registration-attributes.md) | TBD |
| [NDIS50_PROTOCOL_CHARACTERISTICS structure](ns-ndis--ndis50-protocol-characteristics.md) | TBD |
| [MEDIA_SPECIFIC_INFORMATION structure](ns-ndis--media-specific-information.md) | TBD |
| [NET_BUFFER_LIST structure](ns-ndis--net-buffer-list~r1.md) | The NET_BUFFER_LIST structure specifies a linked list of NET_BUFFER structures. |
| [NDIS_PROTOCOL_CO_CHARACTERISTICS structure](ns-ndis--ndis-protocol-co-characteristics.md) | The NDIS_PROTOCOL_CO_CHARACTERISTICS structure specifies CoNDIS entry points for CoNDIS protocol drivers. |
| [NET_BUFFER structure](ns-ndis--net-buffer.md) | TBD |
| [CO_SPECIFIC_PARAMETERS structure](ns-ndis--co-specific-parameters.md) | TBD |
| [NDIS_PACKET structure](ns-ndis--ndis-packet.md) | TBD |
| [NDIS_FILTER_ATTRIBUTES structure](ns-ndis--ndis-filter-attributes.md) | The NDIS_FILTER_ATTRIBUTES structure defines the attributes of a filter module. |
| [NDIS50_MINIPORT_CHARACTERISTICS structure](ns-ndis--ndis50-miniport-characteristics.md) | TBD |
| [NDIS_NBL_MEDIA_SPECIFIC_INFORMATION_EX structure](ns-ndis--ndis-nbl-media-specific-information-ex.md) | The NDIS_NBL_MEDIA_SPECIFIC_INFORMATION_EX structure defines media-specific information that is associated with a NET_BUFFER_LIST structure. |
| [IPSEC_OFFLOAD_V2_ALGORITHM_INFO structure](ns-ndis--ipsec-offload-v2-algorithm-info.md) | The IPSEC_OFFLOAD_V2_ALGORITHM_INFO structure specifies an algorithm that is used for a security association (SA). |
| [NET_BUFFER structure](ns-ndis--net-buffer~r1.md) | The NET_BUFFER structure specifies data that is transmitted or received over the network. |
| [NDIS_IPSEC_PACKET_INFO structure](ns-ndis--ndis-ipsec-packet-info.md) | TBD |
| [CO_CALL_MANAGER_PARAMETERS structure](ns-ndis--co-call-manager-parameters.md) | TBD |
| [NDIS_PD_RECEIVE_QUEUE_COUNTER structure](ns-ndis--ndis-pd-receive-queue-counter.md) | This structure is used to hold counter information for a receive queue. |
| [NDIS_PD_QUEUE_DISPATCH structure](ns-ndis--ndis-pd-queue-dispatch.md) | This structure contains a provider's driver routines for receive or transmit queues. |
| [NDIS_PACKET_STACK structure](ns-ndis--ndis-packet-stack.md) | TBD |
| [NDIS_CLIENT_CHARACTERISTICS structure](ns-ndis--ndis-client-characteristics.md) | TBD |
| [NDIS40_MINIPORT_CHARACTERISTICS structure](ns-ndis--ndis40-miniport-characteristics.md) | TBD |
| [NDIS_EVENT structure](ns-ndis--ndis-event.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [NDIS_MSIX_TABLE_CONFIG enumeration](ne-ndis--ndis-msix-table-config.md) | The NDIS_MSIX_TABLE_OPERATION enumeration identifies the type of MSI-X configuration operation. |
| [NDIS_SHARED_MEMORY_USAGE enumeration](ne-ndis--ndis-shared-memory-usage.md) | The NDIS_SHARED_MEMORY_USAGE enumeration specifies how shared memory is used. |
| [NDIS_INTERFACE_TYPE enumeration](ne-ndis--ndis-interface-type.md) | TBD |
| [NDIS_PD_PROVIDER_CONTROL_CODE enumeration](ne-ndis-ndis-pd-provider-control-code.md) | TBD |
| [NDIS_DEVICE_PNP_EVENT enumeration](ne-ndis--ndis-device-pnp-event.md) | TBD |
| [NDIS_ENVIRONMENT_TYPE enumeration](ne-ndis--ndis-environment-type.md) | TBD |
| [NDIS_SHUTDOWN_ACTION enumeration](ne-ndis--ndis-shutdown-action.md) | TBD |
| [NDIS_PD_CONTROL_TYPE enumeration](ne-ndis-ndis-pd-control-type.md) | TBD |
| [NDIS_CLASS_ID enumeration](ne-ndis--ndis-class-id.md) | TBD |
| [IPSEC_OFFLOAD_V2_OPERATION enumeration](ne-ndis--ipsec-offload-v2-operation.md) | The IPSEC_OFFLOAD_V2_OPERATION enumeration specifies the IPsec operation for which a security association (SA) is used. |
| [NDIS_PER_PACKET_INFO enumeration](ne-ndis--ndis-per-packet-info.md) | TBD |
| [NDIS_NET_BUFFER_LIST_INFO enumeration](ne-ndis--ndis-net-buffer-list-info.md) | The NDIS_NET_BUFFER_LIST_INFO enumeration identifies information that is common to all NET_BUFFER structures in a NET_BUFFER_LIST structure. |
| [NDIS_PD_COUNTER_TYPE enumeration](ne-ndis-ndis-pd-counter-type.md) | The NDIS_PD_COUNTER_TYPE enumeration defines types of PacketDirect Provider Interface (PDPI) counters. Its enumeration values are used in the Type member of the NDIS_PD_COUNTER_PARAMETERS structure. |
| [NDIS_INTERRUPT_TYPE enumeration](ne-ndis--ndis-interrupt-type.md) | TBD |
| [NDIS_POWER_PROFILE enumeration](ne-ndis--ndis-power-profile.md) | TBD |
| [NDIS_TASK enumeration](ne-ndis--ndis-task.md) | TBD |
| [NDIS_PD_QUEUE_CONTROL_CODE enumeration](ne-ndis-ndis-pd-queue-control-code.md) | TBD |
| [NDIS_PD_QUEUE_TYPE enumeration](ne-ndis-ndis-pd-queue-type.md) | The NDIS_PD_QUEUE_TYPE enumeration defines types of PacketDirect Provider Interface (PDPI) queues. Its enumeration values are used in the QueueType member of the NDIS_PD_QUEUE_PARAMETERS structure. |
| [NDIS_PARAMETER_TYPE enumeration](ne-ndis--ndis-parameter-type.md) | The NDIS_PARAMETER_TYPE enumeration type identifies the type of a registry entry. |
| [NDIS_PROCESSOR_TYPE enumeration](ne-ndis--ndis-processor-type.md) | TBD |
| [NDIS_HALT_ACTION enumeration](ne-ndis--ndis-halt-action.md) | TBD |
| [NET_DEVICE_POWER_STATE enumeration](ne-ndis--net-device-power-state.md) | TBD |
| [NDIS_ENCAPSULATION enumeration](ne-ndis--ndis-encapsulation.md) | TBD |
| [NET_PNP_EVENT_CODE enumeration](ne-ndis--net-pnp-event-code.md) | TBD |

This header is used in these topics:

- [netvista](..content/_netvista)
