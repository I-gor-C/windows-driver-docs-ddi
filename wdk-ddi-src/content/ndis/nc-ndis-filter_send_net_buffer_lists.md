---
UID : NC:ndis.FILTER_SEND_NET_BUFFER_LISTS
title : FILTER_SEND_NET_BUFFER_LISTS
author : windows-driver-content
description : NDIS calls the FilterSendNetBufferLists function to allow a filter driver to filter a linked list of NET_BUFFER_LIST structures.Note  You must declare the function by using the FILTER_SEND_NET_BUFFER_LISTS type.
old-location : netvista\filtersendnetbufferlists.htm
old-project : netvista
ms.assetid : 1b3fc0c8-95da-47e5-8ff1-b7967f5148e7
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RxNameCacheInitialize
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : ndis.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.0 and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : FilterSendNetBufferLists
req.alt-loc : Ndis.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : <= DISPATCH_LEVEL
req.typenames : VIDEO_STREAM_INIT_PARMS, *LPVIDEO_STREAM_INIT_PARMS
---


# FILTER_SEND_NET_BUFFER_LISTS function
NDIS calls the 
  <i>FilterSendNetBufferLists</i> function to allow a filter driver to filter a linked list of 
  <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structures.

## Syntax

```
FILTER_SEND_NET_BUFFER_LISTS FilterSendNetBufferLists;

void FilterSendNetBufferLists(
  NDIS_HANDLE FilterModuleContext,
  PNET_BUFFER_LIST NetBufferList,
  NDIS_PORT_NUMBER PortNumber,
  ULONG SendFlags
)
{...}
```

## Parameters

`FilterModuleContext`

A handle to the context area for the filter module. The filter driver created and initialized this
     context area in the 
     <a href="..\ndis\nc-ndis-filter_attach.md">FilterAttach</a> function.

`NetBufferList`



`PortNumber`

A port number that identifies a miniport adapter port. Miniport adapter port numbers are assigned
     by calling the 
     <a href="..\ndis\nf-ndis-ndismallocateport.md">NdisMAllocatePort</a> function. A zero
     value identifies the default port of a miniport adapter.

`SendFlags`

Flags that define attributes for the send operation. The flags can be combined with an OR operation.
      To clear all the flags, set this member to zero. This function supports the following flags:


## Return Value

None

## Remarks

<i>FilterSendNetBufferLists</i> is an optional function. If a filter driver does not filter send requests,
    it can set the entry point for this function to <b>NULL</b> when it calls the 
    <a href="..\ndis\nf-ndis-ndisfregisterfilterdriver.md">
    NdisFRegisterFilterDriver</a> function.

If a filter driver specifies a 
    <i>FilterSendNetBufferLists</i> function and it queues send requests, it must also specify a 
    <a href="..\ndis\nc-ndis-filter_cancel_send_net_buffer_lists.md">
    FilterCancelSendNetBufferLists</a> function.

The filter driver can call the 
    <a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a> function,
    from the 
    <a href="..\ndis\nc-ndis-filter_set_module_options.md">FilterSetModuleOptions</a> function, to
    specify a 
    <i>FilterSendNetBufferLists</i> function for a filter module.

If the filter driver specifies a 
    <i>FilterSendNetBufferLists</i> function, NDIS calls this function to filter the data that is contained in
    a list of 
    <a href="..\ndis\ns-ndis-_net_buffer.md">NET_BUFFER</a> structures over the network. NDIS
    specifies a list of <b>NET_BUFFER</b> structures in each 
    <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structure.

If the filter driver did not specify 
    <i>FilterSendNetBufferLists</i>, NDIS calls the next filter driver that is lower in the driver stack that
    did specify a 
    <i>FilterSendNetBufferLists</i> function. If there are no such underlying filter drivers, NDIS calls an
    underlying driver's 
    <a href="..\ndis\nc-ndis-miniport_send_net_buffer_lists.md">
    MiniportSendNetBufferLists</a> function.

The filter driver can filter the data and send the filtered data to underlying drivers. For each
    <a href="..\ndis\ns-ndis-_net_buffer.md">NET_BUFFER</a> structure submitted to 
    <i>FilterSendNetBufferLists</i>, a filter driver can do the following:

Pass the buffer on to the next underlying driver by calling the 
      <a href="..\ndis\nf-ndis-ndisfsendnetbufferlists.md">NdisFSendNetBufferLists</a> function. The filter driver can modify the buffer contents before calling
      
      <b>NdisFSendNetBufferLists</b>. In this case NDIS calls the 
      <a href="..\ndis\nc-ndis-filter_send_net_buffer_lists_complete.md">
      FilterSendNetBufferListsComplete</a> function after the underlying drivers complete the send
      request.

Reject the buffer by calling the 
      <a href="..\ndis\nf-ndis-ndisfsendnetbufferlistscomplete.md">NdisFSendNetBufferListsComplete</a> function.

Queue the buffer in a local data structure for later processing.

Copy the buffer and originate a send request with the copy. The send operation is similar to a
      filter-driver initiated send request. In this case, the driver must return the original buffer to the
      overlying driver by calling the 
      <a href="..\ndis\nf-ndis-ndisfsendnetbufferlistscomplete.md">NdisFSendNetBufferListsComplete</a> function.

After the send operation is complete, a filter driver reverses the modifications, if any, to the
    buffer descriptors that it made in the 
    <i>FilterSendNetBufferLists</i> function. The driver calls the 
    <a href="..\ndis\nf-ndis-ndisfsendnetbufferlistscomplete.md">NdisFSendNetBufferListsComplete</a> function to return the linked list of <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structures to
    the overlying drivers and to return the final status of the send request.

If a filter module is in the 
    <i>Paused</i> state, the filter driver must not originate any send requests for that filter module. If
    NDIS calls 
    <i>FilterSendNetBufferLists</i>, the driver must not call 
    <a href="..\ndis\nf-ndis-ndisfsendnetbufferlists.md">NdisFSendNetBufferLists</a> to pass on the data until the driver is restarted. The driver should call 
    <a href="..\ndis\nf-ndis-ndisfsendnetbufferlistscomplete.md">NdisFSendNetBufferListsComplete</a> immediately to complete the send operation. It should set the
    complete status in each <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structure to NDIS_STATUS_PAUSED.

NDIS calls 
    <i>FilterSendNetBufferLists</i> at IRQL &lt;= DISPATCH_LEVEL.

To define a <i>FilterSendNetBufferLists</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="https://msdn.microsoft.com/2F3549EF-B50F-455A-BDC7-1F67782B8DCA">Code Analysis for Drivers</a>, <a href="https://msdn.microsoft.com/74feeb16-387c-4796-987a-aff3fb79b556">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.

For example, to define a <i>FilterSendNetBufferLists</i> function that is named "MySendNetBufferLists", use the <b>FILTER_SEND_NET_BUFFER_LISTS</b> type as shown in this code example:

Then, implement your function as follows:

The <b>FILTER_SEND_NET_BUFFER_LISTS</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>FILTER_SEND_NET_BUFFER_LISTS</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/232c4272-0bf0-4a4e-9560-3bceeca8a3e3">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ndis.h (include Ndis.h) |
| **Library** |  |
| **IRQL** | <= DISPATCH_LEVEL |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\ndis\nc-ndis-filter_attach.md">FilterAttach</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter_cancel_send_net_buffer_lists.md">
   FilterCancelSendNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter_send_net_buffer_lists_complete.md">
   FilterSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter_set_module_options.md">FilterSetModuleOptions</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_send_net_buffer_lists.md">MiniportSendNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfsendnetbufferlists.md">NdisFSendNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfsendnetbufferlistscomplete.md">
   NdisFSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfregisterfilterdriver.md">NdisFRegisterFilterDriver</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismallocateport.md">NdisMAllocatePort</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndiswriteeventlogentry.md">NdisWriteEventLogEntry</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis-_net_buffer.md">NET_BUFFER</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FILTER_SEND_NET_BUFFER_LISTS callback function%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>