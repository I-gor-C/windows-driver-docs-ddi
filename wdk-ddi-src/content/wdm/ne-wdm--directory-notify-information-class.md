---
UID: NE.wdm._DIRECTORY_NOTIFY_INFORMATION_CLASS
title: DIRECTORY_NOTIFY_INFORMATION_CLASS
author: windows-driver-content
description: A value that specifies which structure to use to query or set information for a files in a directory.
old-location: ifsk\_directory_notify_information_class.htm
old-project: ifsk
ms.assetid: 77c2515b-f20a-47ac-9564-9eab009cf625
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DIRECTORY_NOTIFY_INFORMATION_CLASS
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# DIRECTORY_NOTIFY_INFORMATION_CLASS enumeration



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>A value that specifies which structure to use to query or set information for a files in a directory.</p>


## -syntax

````
typedef enum _DIRECTORY_NOTIFY_INFORMATION_CLASS { 
  DirectoryNotifyInformation          = 1,
  DirectoryNotifyExtendedInformation
} DIRECTORY_NOTIFY_INFORMATION_CLASS;
````


## -enum-fields
<dl>

### -field <a id="DirectoryNotifyInformation"></a><a id="directorynotifyinformation"></a><a id="DIRECTORYNOTIFYINFORMATION"></a><b>DirectoryNotifyInformation</b>

<dd>
<p>A <b>FILE_NOTIFY_INFORMATION </b>structure.</p>
</dd>

### -field <a id="DirectoryNotifyExtendedInformation"></a><a id="directorynotifyextendedinformation"></a><a id="DIRECTORYNOTIFYEXTENDEDINFORMATION"></a><b>DirectoryNotifyExtendedInformation</b>

<dd>
<p>A <b>FILE_NOTIFY_EXTENDED_INFORMATION</b> structure.</p>
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
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
</table>