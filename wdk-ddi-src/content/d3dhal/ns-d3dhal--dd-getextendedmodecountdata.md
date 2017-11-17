---
UID: NS.d3dhal._DD_GETEXTENDEDMODECOUNTDATA
title: DD_GETEXTENDEDMODECOUNTDATA
author: windows-driver-content
description: DirectX 9.0 and later versions only. DD_GETEXTENDEDMODECOUNTDATA is the data structure pointed to by the lpvData field of DD_GETDRIVERINFODATA for DD_GETDRIVERINFO2DATA queries with the type D3DGDI2_TYPE_GETEXTENDEDMODECOUNT.
old-location: display\dd_getextendedmodecountdata.htm
ms.assetid: 138b6ae2-4c89-40cb-a7b0-d1208e68c460
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dhal.h
req.include-header: D3dhal.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DD_GETEXTENDEDMODECOUNTDATA
req.alt-loc: d3dhal.h
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
ms.keywords: DD_GETEXTENDEDMODECOUNTDATA, DD_GETEXTENDEDMODECOUNTDATA
req.iface: 
---

# DD_GETEXTENDEDMODECOUNTDATA structure



## -description
<p>
   DirectX 9.0 and later versions only.
   </p>
<p>DD_GETEXTENDEDMODECOUNTDATA is the data structure pointed to by the <b>lpvData</b> field of <a href="https://msdn.microsoft.com/library/windows/hardware/ff551550">DD_GETDRIVERINFODATA</a> for DD_GETDRIVERINFO2DATA queries with the type D3DGDI2_TYPE_GETEXTENDEDMODECOUNT.</p>


## -syntax

````
typedef struct _DD_GETEXTENDEDMODECOUNTDATA {
  DD_GETDRIVERINFO2DATA gdi2;
  DWORD                 dwModeCount;
  DWORD                 dwReserved;
} DD_GETEXTENDEDMODECOUNTDATA;
````


## -struct-fields
<dl>

### -field <b>gdi2</b>

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551548">DD_GETDRIVERINFO2DATA</a> structure that contains the <b>GetDriverInfo2</b> data for the query.</p>
</dd>

### -field <b>dwModeCount</b>

<dd>
<p>Receives the number of supported extended display modes.</p>
</dd>

### -field <b>dwReserved</b>

<dd>
<p>Specifies a reserved field. Driver should not read or write.</p>
</dd>
</dl>

## -remarks
<p>To handle D3DGDI2_TYPE_GETEXTENDEDMODECOUNT, the driver must store the number of extended display modes that it supports in the <b>dwModeCount</b> member of DD_GETEXTENDEDMODECOUNTDATA. Display modes are described by D3DDISPLAYMODE structures. For more information about D3DDISPLAYMODE, see the DirectX SDK documentation.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dhal.h (include D3dhal.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551550">DD_GETDRIVERINFODATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551548">DD_GETDRIVERINFO2DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551559">DD_GETEXTENDEDMODEDATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DD_GETEXTENDEDMODECOUNTDATA structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
