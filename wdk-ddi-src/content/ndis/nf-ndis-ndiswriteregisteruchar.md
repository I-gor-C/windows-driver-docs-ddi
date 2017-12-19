---
UID: NF.ndis.NdisWriteRegisterUchar
title: NdisWriteRegisterUchar macro
author: windows-driver-content
description: NdisWriteRegisterUchar is called by the miniport driver to write a UCHAR to a memory-mapped device register.
old-location: netvista\ndiswriteregisteruchar.htm
old-project: NetVista
ms.assetid: 8f720af6-d70a-4682-86f4-011e70a6f64f
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: NdisWriteRegisterUchar
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisWriteRegisterUchar (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisWriteRegisterUchar (NDIS   5.1)) in Windows XP.
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
---

# NdisWriteRegisterUchar macro



## -description
<b>NdisWriteRegisterUchar</b> is called by the miniport driver to write a UCHAR to a memory-mapped device
  register.



## -syntax

````
VOID NdisWriteRegisterUchar(
  [in] PUCHAR Register,
  [in] UCHAR  Data
);
````


## -parameters

### -param Register [in]

Pointer to the memory-mapped register. This virtual address must fall within a range returned by
     an initialization-time call to 
     <a href="netvista.ndismmapiospace">NdisMMapIoSpace</a>.


### -param Data [in]

Specifies the caller-supplied UCHAR that this function transfers to the 
     <i>Register</i> .


## -remarks
If a driver calls this function, a NIC's device registers must be mapped to noncached memory during
    driver initialization.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/c650d640-6efb-4ddf-9f48-113c8379aab7">NdisWriteRegisterUchar (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisWriteRegisterUchar (NDIS
   5.1)</b>) in Windows XP.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="netvista.ndismmapiospace">NdisMMapIoSpace</a>
</dt>
<dt>
<a href="netvista.ndisreadregisteruchar">NdisReadRegisterUchar</a>
</dt>
<dt>
<a href="netvista.ndiswriteregisterulong">NdisWriteRegisterUlong</a>
</dt>
<dt>
<a href="netvista.ndiswriteregisterushort">NdisWriteRegisterUshort</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NdisWriteRegisterUchar macro%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

