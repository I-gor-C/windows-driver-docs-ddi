---
UID: NS.ndischimney._NDIS_OFFLOAD_HANDLE
title: NDIS_OFFLOAD_HANDLE
author: windows-driver-content
description: The NDIS_OFFLOAD_HANDLE structure represents a driver's context for an offloaded state object.
old-location: netvista\ndis_offload_handle.htm
old-project: netvista
ms.assetid: cc1d7ca2-273a-42ca-896c-aebee862a4cd
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_OFFLOAD_HANDLE, NDIS_OFFLOAD_HANDLE, *PNDIS_OFFLOAD_HANDLE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndischimney.h
req.include-header: Ndischimney.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_OFFLOAD_HANDLE
req.alt-loc: ndischimney.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# NDIS_OFFLOAD_HANDLE structure



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>The NDIS_OFFLOAD_HANDLE structure represents a driver's context for an offloaded state object.</p>


## -syntax

````
typedef struct _NDIS_OFFLOAD_HANDLE {
  PVOID NdisReserved[1];
  PVOID MiniportOffloadContext;
} NDIS_OFFLOAD_HANDLE, *PNDIS_OFFLOAD_HANDLE;
````


## -struct-fields
<dl>

### -field <b>NdisReserved</b>

<dd>
<p>Reserved for use by NDIS.</p>
</dd>

### -field <b>MiniportOffloadContext</b>

<dd>
<p>A pointer that references a host memory location into which the underlying driver writes a PVOID
     value when completing the initiate offload operation. This PVOID value references the underlying
     driver's offload context for the offloaded state object.</p>
</dd>
</dl>

## -remarks
<p>When propagating the offload of a TCP chimney state object, an intermediate driver supplies a pointer
    to an NDIS_OFFLOAD_HANDLE structure. This pointer, in effect, references the intermediate driver's
    context for the offloaded state object.</p>

<p>The NDIS_OFFLOAD_HANDLE structure contains a 
    <b>MiniportOffloadContext</b> pointer that references a memory location into which the underlying driver
    or offload target writes a PVOID value before completing the initiate offload operation. This PVOID value
    references the underlying driver's or offload target's context for the offloaded state object.</p>

<p>For more information about the use of the NDIS_OFFLOAD_HANDLE structure, see 
    <a href="netvista.referencing_offloaded_state_through_an_intermediate_driver">
    Referencing Offloaded State Through an Intermediate Driver</a>.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\ndischimney\nc-ndischimney-w-initiate-offload-handler.md">MiniportInitiateOffload</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563604">NdisMInitiateOffloadComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_OFFLOAD_HANDLE structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
