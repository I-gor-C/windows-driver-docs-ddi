---
UID: NS.wiamindr_lh._WIA_DEV_CAP_DRV
title: WIA_DEV_CAP_DRV
author: windows-driver-content
description: The WIA_DEV_CAP_DRV structure is used to enumerate device capabilities. A device capability is defined by an event or command that the device supports.
old-location: image\wia_dev_cap_drv.htm
old-project: image
ms.assetid: 4024d455-2393-481f-8cb5-b33346ca85c7
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WIA_DEV_CAP_DRV, WIA_DEV_CAP_DRV
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WIA_DEV_CAP_DRV
req.alt-loc: wiamindr_lh.h
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
req.iface: IWiaMiniDrvTransferCallback
req.product: Windows 10 or later.
---

# WIA_DEV_CAP_DRV structure



## -description
<p>The WIA_DEV_CAP_DRV structure is used to enumerate device capabilities. A device capability is defined by an event or command that the device supports.</p>


## -syntax

````
typedef struct _WIA_DEV_CAP_DRV {
  GUID     *guid;
  ULONG    ulFlags;
  LPOLESTR wszName;
  LPOLESTR wszDescription;
  LPOLESTR wszIcon;
} WIA_DEV_CAP_DRV, *PWIA_DEV_CAP_DRV;
````


## -struct-fields
<dl>

### -field <b>guid</b>

<dd>
<p>Points to a GUID that identifies the device capability. This member can be set to any of the values specified for WIA device commands (WIA_CMD_<i>XXX</i> commands) or WIA event identifiers (WIA_EVENT_<i>XXX</i> event identifiers). See the Microsoft Windows SDK documentation for more information.</p>
<p>The driver can define its own capability GUID that it can send down to the device. An application would need to have specific knowledge about that capability in order for it to be able to respond to the new capability, however. An application normally recognizes only the standard WIA command and event GUIDs (WIA_CMD_XXX and WIA_EVENT_XXX).</p>
</dd>

### -field <b>ulFlags</b>

<dd>
<p>Specifies the type of event. This member can be set to one or both of the following: </p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WIA_ACTION_EVENT</p>
</td>
<td>
<p>Application can register action for the given event using the <b>IWiaDevMgr::RegisterEventCallbackProgram</b> and <b>IwiaDevMgr::RegisterEventCallbackCLSID</b> methods, which are described in the Windows SDK documentation. An action event launches the application that is registered to handle such an event.</p>
</td>
</tr>
<tr>
<td>
<p>WIA_NOTIFICATION_EVENT</p>
</td>
<td>
<p>Application can register for notification on the given event using the <b>IwiaDevMgr::RegisterEventCallbackInterface</b> method (described in the Windows SDK documentation). A notification event is sent only to applications that are already running.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>wszName</b>

<dd>
<p>Specifies a string that contains a short version of the capability name. </p>
</dd>

### -field <b>wszDescription</b>

<dd>
<p>Specifies a string containing the version of the capability name that can be displayed to the user.</p>
</dd>

### -field <b>wszIcon</b>

<dd>
<p>Specifies a string containing the name of the icon for this capability. The icon can be displayed to the user .</p>
</dd>
</dl>

## -remarks
<p>The WIA service calls the minidriver's <a href="image.iwiaminidrv_drvgetcapabilities">IWiaMiniDrv::drvGetCapabilities</a> function to fill in the members of a WIA_DEV_CAP_DRV structure.</p>

<p>When a driver is enumerating event handlers, the only valid value is WIA_IS_DEFAULT_HANDLER; which indicates that the currently registered handler should be used.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Me and in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamindr_lh.h (include Wiamindr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="image.iwiaminidrv_drvgetcapabilities">IWiaMiniDrv::drvGetCapabilities</a>
</dt>
<dt>
<a href="NULL">Driver Capabilities</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20WIA_DEV_CAP_DRV structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
