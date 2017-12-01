---
UID: NS.ndis.BINARY_DATA
title: BINARY_DATA
author: windows-driver-content
description: The BINARY_DATA structure contains the binary data of a named entry in the registry.
old-location: netvista\binary_data.htm
old-project: netvista
ms.assetid: 2d629905-49aa-4b66-83f3-0aecb72b73ea
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BINARY_DATA, BINARY_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers in Windows Vista. Supported for NDIS   5.1 drivers in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BINARY_DATA
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

# BINARY_DATA structure



## -description
<p>The BINARY_DATA structure contains the binary data of a named entry in the registry.</p>


## -syntax

````
typedef struct {
  USHORT Length;
  PVOID  Buffer;
} BINARY_DATA;
````


## -struct-fields
<dl>

### -field <b>Length</b>

<dd>
<p>The length, in bytes, of the data that the 
     <b>Buffer</b> member points to.</p>
</dd>

### -field <b>Buffer</b>

<dd>
<p>Pointer to a buffer containing the binary data.</p>
</dd>
</dl>

## -remarks
<p>The BINARY_DATA structure is used in the 
    <b>ParameterData</b> member of the 
    <a href="..\ndis\ns-ndis--ndis-configuration-parameter.md">
    NDIS_CONFIGURATION_PARAMETER</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers in Windows Vista. Supported for NDIS
   5.1 drivers in Windows XP.</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\ns-ndis--ndis-configuration-parameter.md">NDIS_CONFIGURATION_PARAMETER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20BINARY_DATA structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
