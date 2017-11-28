---
UID: NS.d3dkmthk._D3DKMT_ACTIVATE_SPECIFIC_DIAG_ESCAPE
title: D3DKMT_ACTIVATE_SPECIFIC_DIAG_ESCAPE
author: windows-driver-content
description: Indicates an escape type that is to be activated or deactivated.
old-location: display\d3dkmt_activate_specific_diag_escape.htm
old-project: display
ms.assetid: e3c61b33-2e10-42cf-b9e8-fe70a43573e8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_ACTIVATE_SPECIFIC_DIAG_ESCAPE, D3DKMT_ACTIVATE_SPECIFIC_DIAG_ESCAPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_ACTIVATE_SPECIFIC_DIAG_ESCAPE
req.alt-loc: D3dkmthk.h
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

# D3DKMT_ACTIVATE_SPECIFIC_DIAG_ESCAPE structure



## -description
<p>Indicates an escape type that is to be activated or deactivated.</p>


## -syntax

````
typedef struct _D3DKMT_ACTIVATE_SPECIFIC_DIAG_ESCAPE {
  D3DKMT_ESCAPETYPE Type;
  BOOL              Activate;
} D3DKMT_ACTIVATE_SPECIFIC_DIAG_ESCAPE;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>The <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-escape.md">D3DKMT_ESCAPETYPE</a> escape type  that needs to be activated or deactivated.</p>
</dd>

### -field <b>Activate</b>

<dd>
<p>If <b>TRUE</b>, the escape type is to be activated. If <b>FALSE</b>, the escape type is to be deactivated.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-escape.md">D3DKMT_ESCAPETYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_ACTIVATE_SPECIFIC_DIAG_ESCAPE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
