---
UID: NF.ndis.NdisRetrieveUlong
title: NdisRetrieveUlong
author: windows-driver-content
description: The NdisRetrieveUlong function retrieves a ULONG value from the source address, avoiding alignment faults.
old-location: netvista\ndisretrieveulong.htm
old-project: netvista
ms.assetid: 41788885-d8a1-4459-82a0-261b39862530
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisRetrieveUlong
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for existing drivers in  NDIS 6.0 and later, but new drivers should use RtlRetrieveUlong instead.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisRetrieveUlong
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
req.irql: See Remarks section
req.iface: 
---

# NdisRetrieveUlong function



## -description
<p>The 
  <b>NdisRetrieveUlong</b> function retrieves a ULONG value from the source address, avoiding alignment
  faults.</p>


## -syntax

````
VOID NdisRetrieveUlong(
  _In_ PULONG DestinationAddress,
  _In_ PULONG SourceAddress
);
````


## -parameters
<dl>

### -param <i>DestinationAddress</i> [in]

<dd>
<p>A pointer to a ULONG-aligned memory location in which to store the value.</p>
</dd>

### -param <i>SourceAddress</i> [in]

<dd>
<p>A pointer to a memory location from which to retrieve the ULONG value.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The given 
    <i>DestinationAddress</i> is assumed to be aligned on a ULONG boundary.</p>

<p>Callers of 
    <b>NdisRetrieveUlong</b> can be running at any IRQL if the given addresses are in nonpaged pool.
    Otherwise, callers must be running at IRQL &lt; DISPATCH_LEVEL.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p> Supported for existing drivers in  NDIS 6.0 and later, but new drivers should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff562756">RtlRetrieveUlong</a> instead.</p>
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
<p>See Remarks section</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nf-ndis-ndisstoreulong.md">NdisStoreUlong</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisRetrieveUlong function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
