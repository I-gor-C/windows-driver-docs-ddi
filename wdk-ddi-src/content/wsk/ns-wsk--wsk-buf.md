---
UID: NS.wsk._WSK_BUF
title: WSK_BUF
author: windows-driver-content
description: The WSK_BUF structure defines a data buffer that is used for sending and receiving data over a socket.
old-location: netvista\wsk_buf.htm
old-project: netvista
ms.assetid: bef653d3-5de3-4af3-8c1f-cff55619e2e9
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WSK_BUF, WSK_BUF, *PWSK_BUF
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wsk.h
req.include-header: Wsk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WSK_BUF
req.alt-loc: wsk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WSK_BUF structure



## -description
<p>The WSK_BUF structure defines a data buffer that is used for sending and receiving data over a
  socket.</p>


## -syntax

````
typedef struct _WSK_BUF {
  PMDL   Mdl;
  ULONG  Offset;
  SIZE_T Length;
} WSK_BUF, *PWSK_BUF;
````


## -struct-fields
<dl>

### -field <b>Mdl</b>

<dd>
<p>A pointer to a memory descriptor list (MDL). The MDL can be a single MDL or the first MDL in an
     MDL chain. If the 
     <b>Length</b> member is zero, this pointer can be <b>NULL</b>.</p>
</dd>

### -field <b>Offset</b>

<dd>
<p>An offset to where the data starts in the MDL. If the 
     <b>Mdl</b> member points to the first MDL in an MDL chain, this offset must be within the memory buffer
     that is described by the first MDL in the chain. If the 
     <b>Mdl</b> member is <b>NULL</b>, the 
     <b>Offset</b> member is not used.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>When a WSK_BUF structure is used to describe a buffer of data to be sent over a socket, this
     member specifies the number of bytes of data in the MDL (or MDL chain) to be sent.
     </p>
<p>When a WSK_BUF structure is used to describe a buffer for receiving data from a socket, this member
     specifies the maximum number of bytes to be received into the MDL (or MDL chain).</p>
<p>When a WSK_BUF structure is contained within either a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571165">WSK_DATA_INDICATION</a> structure or a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571164">WSK_DATAGRAM_INDICATION</a> structure,
     this member specifies the number of bytes of received data in the MDL (or MDL chain).</p>
</dd>
</dl>

## -remarks
<p>Each MDL in the MDL chain that is pointed to by the 
    <b>Mdl</b> member describes memory that is either locked or from non-paged pool.</p>

<p>When a WSK application passes a pointer to a WSK_BUF structure to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff571139">WskReceive</a> function, the application can
    specify zero for the 
    <b>Length</b> member of the structure. In that situation, the 
    <b>Mdl</b> member can be <b>NULL</b> because no data will be copied into the buffer.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wsk.h (include Wsk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571129">WskDisconnect</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571139">WskReceive</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571141">WskReceiveFrom</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571146">WskSend</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571148">WskSendTo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571165">WSK_DATA_INDICATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571164">WSK_DATAGRAM_INDICATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WSK_BUF structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
