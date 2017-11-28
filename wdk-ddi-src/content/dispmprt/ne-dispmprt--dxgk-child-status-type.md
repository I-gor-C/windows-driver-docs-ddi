---
UID: NE.dispmprt._DXGK_CHILD_STATUS_TYPE
title: DXGK_CHILD_STATUS_TYPE
author: windows-driver-content
description: The DXGK_CHILD_STATUS_TYPE enumeration indicates the type of status being requested or reported for a child device of the display adapter.
old-location: display\dxgk_child_status_type.htm
old-project: display
ms.assetid: 5fa4b7e2-8215-49d8-9d70-b45c972b39b4
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_CHILD_STATUS_TYPE
req.alt-loc: dispmprt.h
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
req.iface: IDebugSystemObjects4
---

# DXGK_CHILD_STATUS_TYPE enumeration



## -description
<p>The DXGK_CHILD_STATUS_TYPE enumeration indicates the type of status being requested or reported for a child device of the display adapter.</p>


## -syntax

````
typedef enum _DXGK_CHILD_STATUS_TYPE { 
  StatusUninitialized,
  StatusConnection,
  StatusRotation,
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
  StatusMiracast

#endif } DXGK_CHILD_STATUS_TYPE, *PDXGK_CHILD_STATUS_TYPE;
````


## -enum-fields
<dl>

### -field <a id="StatusUninitialized"></a><a id="statusuninitialized"></a><a id="STATUSUNINITIALIZED"></a><b>StatusUninitialized</b>

<dd>
<p>Indicates that a variable of type DXGK_CHILD_STATUS_TYPE has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="StatusConnection"></a><a id="statusconnection"></a><a id="STATUSCONNECTION"></a><b>StatusConnection</b>

<dd>
<p>Indicates that the request or report pertains to whether the child device has a monitor (or other display device) connected to it.</p>
</dd>

### -field <a id="StatusRotation"></a><a id="statusrotation"></a><a id="STATUSROTATION"></a><b>StatusRotation</b>

<dd>
<p>Indicates that the request or report pertains to the rotation angle of the monitor (or other display device) that is connected to the child device.</p>
</dd>

### -field <a id="StatusMiracast"></a><a id="statusmiracast"></a><a id="STATUSMIRACAST"></a><b>StatusMiracast</b>

<dd>
<p>Indicates that the request or report pertains to a monitor (or other display device) that is connected wirelessly to the child device through a Miracast connected session.</p>
<p>Supported by WDDM 1.3 and later drivers running on Windows 8.1 and later.</p>
</dd>
</dl>

## -remarks
<p>The <b>Type</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561010">DXGK_CHILD_STATUS</a> structure is a member of the <b>DXGK_CHILD_STATUS_TYPE</b> enumeration.</p>

<p>The <b>Type</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561010">DXGK_CHILD_STATUS</a> structure is a member of the <b>DXGK_CHILD_STATUS_TYPE</b> enumeration.</p>

<p>The <b>Type</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561010">DXGK_CHILD_STATUS</a> structure is a member of the <b>DXGK_CHILD_STATUS_TYPE</b> enumeration.</p>

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
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgkddiquerychildstatus">DxgkDdiQueryChildStatus</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkcb-indicate-child-status.md">DxgkCbIndicateChildStatus</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_CHILD_STATUS_TYPE enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
