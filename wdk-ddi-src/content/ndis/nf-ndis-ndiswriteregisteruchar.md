---
UID: NF.ndis.NdisWriteRegisterUchar
title: NdisWriteRegisterUchar
author: windows-driver-content
description: NdisWriteRegisterUchar is called by the miniport driver to write a UCHAR to a memory-mapped device register.
old-location: netvista\ndiswriteregisteruchar.htm
old-project: netvista
ms.assetid: 8f720af6-d70a-4682-86f4-011e70a6f64f
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisWriteRegisterUchar
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisWriteRegisterUchar (NDIS
   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisWriteRegisterUchar (NDIS
   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisWriteRegisterUchar
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.iface: 
---

# NdisWriteRegisterUchar function



## -description
<p><b>NdisWriteRegisterUchar</b> is called by the miniport driver to write a UCHAR to a memory-mapped device
  register.</p>


## -syntax

````
VOID NdisWriteRegisterUchar(
  _In_ PUCHAR Register,
  _In_ UCHAR  Data
);
````


## -parameters
<dl>

### -param <i>Register</i> [in]

<dd>
<p>Pointer to the memory-mapped register. This virtual address must fall within a range returned by
     an initialization-time call to 
     <a href="https://msdn.microsoft.com/library/windows/hardware/hh975119">NdisMMapIoSpace</a>.</p>
</dd>

### -param <i>Data</i> [in]

<dd>
<p>Specifies the caller-supplied UCHAR that this function transfers to the 
     <i>Register</i> .</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If a driver calls this function, a NIC's device registers must be mapped to noncached memory during
    driver initialization.</p>

<p>If a driver calls this function, a NIC's device registers must be mapped to noncached memory during
    driver initialization.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/c650d640-6efb-4ddf-9f48-113c8379aab7">NdisWriteRegisterUchar (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisWriteRegisterUchar (NDIS
   5.1)</b>) in Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975119">NdisMMapIoSpace</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564513">NdisReadRegisterUchar</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564683">NdisWriteRegisterUlong</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564685">NdisWriteRegisterUshort</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisWriteRegisterUchar function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
