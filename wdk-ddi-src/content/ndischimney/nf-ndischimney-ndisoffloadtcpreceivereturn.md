---
UID: NF.ndischimney.NdisOffloadTcpReceiveReturn
title: NdisOffloadTcpReceiveReturn
author: windows-driver-content
description: A protocol driver or intermediate driver calls the NdisOffloadTcpReceiveReturn function to return ownership of NET_BUFFER_LIST and associated structures to an underlying offload target.
old-location: netvista\ndisoffloadtcpreceivereturn.htm
old-project: netvista
ms.assetid: 39f541be-c514-4cd4-bf7d-03b7a318b663
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisOffloadTcpReceiveReturn
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndischimney.h
req.include-header: Ndischimney.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisOffloadTcpReceiveReturn
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: 
req.iface: 
---

# NdisOffloadTcpReceiveReturn function



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>A protocol driver or intermediate driver calls the 
  <b>NdisOffloadTcpReceiveReturn</b> function to return ownership of NET_BUFFER_LIST and associated structures
  to an underlying offload target.</p>


## -syntax

````
VOID NdisOffloadTcpReceiveReturn(
  _In_ NDIS_HANDLE      NdisBindingHandle,
  _In_ PNET_BUFFER_LIST NetBufferList
);
````


## -parameters
<dl>

### -param <i>NdisBindingHandle</i> [in]

<dd>
<p>The handle that NDIS provided at the 
     <i>NdisBindingHandle</i> parameter of the 
     <a href="..\ndis\nf-ndis-ndisopenadapterex.md">NdisOpenAdapterEx</a> function. This handle
     identifies the binding between the caller and the underlying intermediate driver or offload
     target.</p>
</dd>

### -param <i>NetBufferList</i> [in]

<dd>
<p>A pointer to a 
     <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure. This structure
     can be a stand-alone structure or the first structure in a linked list of NET_BUFFER_LIST structures.
     The linked list can contain NET_BUFFER_LIST structures from one or more calls to the 
     <a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-receive-indicate.md">
     NdisTcpOffloadReceiveHandler</a> function.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>NdisOffloadTcpReceiveReturn</b> function always returns NDIS_STATUS_SUCCESS. The receive return
     operation is always completed synchronously.</p>

## -remarks
<p>In response to a call to its 
    <a href="..\ndischimney\nc-ndischimney-w-tcp-offload-receive-return-handler.md">
    MiniportTcpOffloadReceiveReturn</a> function, an intermediate driver calls the 
    <b>NdisOffloadTcpReceiveReturn</b> function to propagate the receive return operation to the underlying
    intermediate driver or offload target. For more information, see 
    <a href="NULL">Propagating I/O Operations</a>.</p>

<p>To the 
    <b>NdisOffloadTcpReceiveReturn</b> function, the intermediate driver passes the following:</p>

<p>An 
      <i>NdisOffloadHandle</i> function that references the NDIS_OFFLOAD_HANDLE structure stored in the
      intermediate driver's context for the offloaded TCP connection. For more information, see 
      <a href="netvista.referencing_offloaded_state_through_an_intermediate_driver">
      Referencing Offloaded State Through an Intermediate Driver</a>.</p>

<p>The same PNET_BUFFER_LIST pointer that NDIS passed to the intermediate driver's 
      <i>MiniportTcpOffloadReceiveReturn</i> function.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndischimney.h (include Ndischimney.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndischimney\nc-ndischimney-w-tcp-offload-receive-return-handler.md">
   MiniportTcpOffloadReceiveReturn</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--ndis-offload-handle.md">NDIS_OFFLOAD_HANDLE</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-receive-indicate.md">NdisTcpOffloadReceiveHandler</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisOffloadTcpReceiveReturn function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
