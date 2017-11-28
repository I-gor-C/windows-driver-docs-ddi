---
UID: NF.storport.StorPortIsCurrentOsInstallationUpgrade
title: StorPortIsCurrentOsInstallationUpgrade
author: windows-driver-content
description: The StorPortIsCurrentOsInstallationUpgrade routine checks if the current installation of Windows is an upgrade from a previous version or not.
old-location: storage\storportiscurrentosinstallationupgrade.htm
old-project: storage
ms.assetid: 68D944D9-1A52-4FB0-B2D7-9680AB1EDABB
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortIsCurrentOsInstallationUpgrade
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available in starting with Windows 8.1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortIsCurrentOsInstallationUpgrade
req.alt-loc: storport.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: IRQL == PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# StorPortIsCurrentOsInstallationUpgrade function



## -description
<p>The <b>StorPortIsCurrentOsInstallationUpgrade</b>  routine checks if the current installation of Windows is an upgrade from a previous version or not.</p>


## -syntax

````
ULONG StorPortIsCurrentOsInstallationUpgrade(
  _In_  PVOID   HwDeviceExtension,
  _Out_ BOOLEAN *Upgraded
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param <i>Upgraded</i> [out]

<dd>
<p>The value pointed to by <i>Upgraded</i> is set to <b>TRUE</b> if the current operating system installation was upgraded from a previous version. Otherwise, it is set to <b>FALSE</b>.</p>
</dd>
</dl>

## -returns
<p>The <b>StorPortIsCurrentOsInstallationUpgrade</b> routine returns one of these status codes:</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>An upgrade status is returned in the value pointed to by the  <i>Upgraded</i> parameter.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The pointer value  in <i>Upgraded</i> is NULL.</p><dl>
<dt><b>STOR_STATUS_INVALID_IRQL</b></dt>
</dl><p>The current IRQL &gt; PASSIVE_LEVEL.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in starting with Windows 8.1.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>IRQL == PASSIVE_LEVEL</p>
</td>
</tr>
</table>