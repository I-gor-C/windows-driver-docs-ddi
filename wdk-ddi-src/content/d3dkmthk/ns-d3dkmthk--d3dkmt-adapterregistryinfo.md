---
UID: NS.d3dkmthk._D3DKMT_ADAPTERREGISTRYINFO
title: D3DKMT_ADAPTERREGISTRYINFO
author: windows-driver-content
description: The D3DKMT_ADAPTERREGISTRYINFO structure contains registry information about the graphics adapter.
old-location: display\d3dkmt_adapterregistryinfo.htm
old-project: display
ms.assetid: b1bad6e8-8592-457a-8f66-40fc5040ae96
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_ADAPTERREGISTRYINFO, D3DKMT_ADAPTERREGISTRYINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_ADAPTERREGISTRYINFO
req.alt-loc: d3dkmthk.h
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

# D3DKMT_ADAPTERREGISTRYINFO structure



## -description
<p>The D3DKMT_ADAPTERREGISTRYINFO structure contains registry information about the graphics adapter. </p>


## -syntax

````
typedef struct _D3DKMT_ADAPTERREGISTRYINFO {
  WCHAR AdapterString[MAX_PATH];
  WCHAR BiosString[MAX_PATH];
  WCHAR DacType[MAX_PATH];
  WCHAR ChipType[MAX_PATH];
} D3DKMT_ADAPTERREGISTRYINFO;
````


## -struct-fields
<dl>

### -field <b>AdapterString</b>

<dd>
<p>[out] A string that contains the name of the graphics adapter.</p>
</dd>

### -field <b>BiosString</b>

<dd>
<p>[out] A string that contains the name of the BIOS for the graphics adapter.</p>
</dd>

### -field <b>DacType</b>

<dd>
<p>[out] A string that contains the DAC type for the graphics adapter.</p>
</dd>

### -field <b>ChipType</b>

<dd>
<p>[out] A string that contains the chip type for the graphics adapter.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-queryadapterinfo.md">D3DKMT_QUERYADAPTERINFO</a>
</dt>
<dt>
<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtqueryadapterinfo.md">D3DKMTQueryAdapterInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_ADAPTERREGISTRYINFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
