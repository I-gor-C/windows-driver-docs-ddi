---
UID: NS.ndischimney._PATH_OFFLOAD_STATE_CONST
title: PATH_OFFLOAD_STATE_CONST
author: windows-driver-content
description: The PATH_OFFLOAD_STATE_CONST structure contains the constant variables of a path state object.
old-location: netvista\path_offload_state_const.htm
old-project: netvista
ms.assetid: a71f70f6-7731-457b-bd6d-b4a649f76f8b
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: PATH_OFFLOAD_STATE_CONST, PATH_OFFLOAD_STATE_CONST, *PPATH_OFFLOAD_STATE_CONST
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
req.alt-api: PATH_OFFLOAD_STATE_CONST
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

# PATH_OFFLOAD_STATE_CONST structure



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>The PATH_OFFLOAD_STATE_CONST structure contains the constant variables of a path state object.</p>


## -syntax

````
typedef struct _PATH_OFFLOAD_STATE_CONST {
  OFFLOAD_STATE_HEADER Header;
  const UCHAR          *SourceAddress;
  const UCHAR          *DestinationAddress;
} PATH_OFFLOAD_STATE_CONST, *PPATH_OFFLOAD_STATE_CONST;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>An 
     <a href="..\ndischimney\ns-ndischimney--offload-state-header.md">OFFLOAD_STATE_HEADER</a> structure. NDIS
     sets the 
     <b>Length</b> member of 
     <b>Header</b> to the size, in bytes, of the PATH_OFFLOAD_STATE_CONST structure. The 
     <b>RecognizedOptions</b> member of 
     <b>Header</b> is reserved.</p>
</dd>

### -field SourceAddress

<dd>
<p>A pointer to the source IP address of a TCP connection. If the TCP connection is over IPv4, the
     address is a 4-byte IPv4 address. If the TCP connection is over IPv6, the address is a 16-byte IPv6
     address. The source address bytes are always in network byte order.</p>
</dd>

### -field DestinationAddress

<dd>
<p>A pointer to the destination IP address of a TCP connection. If the TCP connection is over IPv4,
     the address is a 4-byte IPv4 address. If the TCP connection is over IPv6, the address is a 16-byte IPv6
     address. The destination address bytes are always in network byte order.</p>
</dd>
</dl>

## -remarks
<p>The value of each path constant variable does not change during the life of a TCP connection. Neither
    the host stack nor the offload target changes the values of a path constant variable. When the host stack
    terminates the offload of the path state object by causing NDIS to call the offload target's 
    <a href="..\ndischimney\nc-ndischimney-w-terminate-offload-handler.md">
    MiniportTerminateOffload</a> function, the offload target does not return the value of the offloaded
    path constant variables to the host stack.</p>

<p>When passed to an offload target, a PATH_OFFLOAD_STATE_CONST structure is associated with an 
    <a href="..\ndischimney\ns-ndischimney--ndis-miniport-offload-block-list.md">
    NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a> structure, which contains a header that is formatted as an 
    <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure. The 
    <b>Revision</b> member of the NDIS_OBJECT_HEADER structure, in this case, specifies the revision number of
    the PATH_OFFLOAD_STATE_CONST structure.</p>

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
<a href="..\ndischimney\nc-ndischimney-w-terminate-offload-handler.md">MiniportTerminateOffload</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--offload-state-header.md">OFFLOAD_STATE_HEADER</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--path-offload-state-cached.md">PATH_OFFLOAD_STATE_CACHED</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--path-offload-state-delegated.md">PATH_OFFLOAD_STATE_DELEGATED</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PATH_OFFLOAD_STATE_CONST structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
