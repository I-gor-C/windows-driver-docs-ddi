---
UID: NE.d3dkmddi._DXGK_PRESENT_DISPLAY_ONLY_PROGRESS_ID
title: DXGK_PRESENT_DISPLAY_ONLY_PROGRESS_ID
author: windows-driver-content
description: Indicates the status of the current present operation.
old-location: display\dxgk_present_display_only_progress_id.htm
ms.assetid: 38023aaf-754a-4b16-96fc-6fd3d48233c3
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_PRESENT_DISPLAY_ONLY_PROGRESS_ID
req.alt-loc: D3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
req.iface: 
---

# DXGK_PRESENT_DISPLAY_ONLY_PROGRESS_ID enumeration



## -description
<p>Indicates the status of the current present operation.</p>


## -syntax

````
typedef enum _DXGK_PRESENT_DISPLAY_ONLY_PROGRESS_ID { 
  DXGK_PRESENT_DISPLAYONLY_PROGRESS_ID_COMPLETE  = 0,
  DXGK_PRESENT_DISPLAYONLY_PROGRESS_ID_FAILED    = 1
} DXGK_PRESENT_DISPLAY_ONLY_PROGRESS_ID;
````


## -enum-fields
<dl>

### -field <a id="DXGK_PRESENT_DISPLAYONLY_PROGRESS_ID_COMPLETE"></a><a id="dxgk_present_displayonly_progress_id_complete"></a><b>DXGK_PRESENT_DISPLAYONLY_PROGRESS_ID_COMPLETE</b>

<dd>
<p>The present operation has completed.</p>
</dd>

### -field <a id="DXGK_PRESENT_DISPLAYONLY_PROGRESS_ID_FAILED"></a><a id="dxgk_present_displayonly_progress_id_failed"></a><b>DXGK_PRESENT_DISPLAYONLY_PROGRESS_ID_FAILED</b>

<dd>
<p>An error occurred during the present operation.</p>
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
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451245">DXGKARGCB_PRESENT_DISPLAYONLY_PROGRESS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_PRESENT_DISPLAY_ONLY_PROGRESS_ID enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
