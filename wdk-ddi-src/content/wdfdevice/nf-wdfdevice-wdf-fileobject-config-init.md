---
UID: NF.wdfdevice.WDF_FILEOBJECT_CONFIG_INIT
title: WDF_FILEOBJECT_CONFIG_INIT
author: windows-driver-content
description: The WDF_FILEOBJECT_CONFIG_INIT function initializes a driver's WDF_FILEOBJECT_CONFIG structure.
old-location: wdf\wdf_fileobject_config_init.htm
old-project: wdf
ms.assetid: 87ad817a-4a62-4061-949c-fe45bdfb44d5
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_FILEOBJECT_CONFIG_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_FILEOBJECT_CONFIG_INIT
req.alt-loc: wdfdevice.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# WDF_FILEOBJECT_CONFIG_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_FILEOBJECT_CONFIG_INIT</b> function initializes a driver's <a href="..\wdfdevice\ns-wdfdevice--wdf-fileobject-config.md">WDF_FILEOBJECT_CONFIG</a> structure.</p>


## -syntax

````
VOID WDF_FILEOBJECT_CONFIG_INIT(
  _Out_    PWDF_FILEOBJECT_CONFIG     FileEventCallbacks,
  _In_opt_ PFN_WDF_DEVICE_FILE_CREATE EvtDeviceFileCreate,
  _In_opt_ PFN_WDF_FILE_CLOSE         EvtFileClose,
  _In_opt_ PFN_WDF_FILE_CLEANUP       EvtFileCleanup
);
````


## -parameters
<dl>

### -param FileEventCallbacks [out]

<dd>
<p>A pointer to a driver-allocated <a href="..\wdfdevice\ns-wdfdevice--wdf-fileobject-config.md">WDF_FILEOBJECT_CONFIG</a> structure.</p>
</dd>

### -param EvtDeviceFileCreate [in, optional]

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-file-create.md">EvtDeviceFileCreate</a> event callback function.</p>
</dd>

### -param EvtFileClose [in, optional]

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-file-close.md">EvtFileClose</a> event callback function.</p>
</dd>

### -param EvtFileCleanup [in, optional]

<dd>
<p>A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-file-cleanup.md">EvtFileCleanup</a> event callback function.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>WDF_FILEOBJECT_CONFIG_INIT</b> function sets the specified <a href="..\wdfdevice\ns-wdfdevice--wdf-fileobject-config.md">WDF_FILEOBJECT_CONFIG</a> structure's <b>Size</b> member, stores the specified callback function pointers, sets the <b>FileObjectClass</b> member to <b>WdfFileObjectWdfCannotUseFsContexts</b>, and sets the <b>AutoForwardCleanupClose</b> member to <b>WdfUseDefault</b>. </p>

<p>For a code example that uses <b>WDF_FILEOBJECT_CONFIG_INIT</b>, see <a href="..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetfileobjectconfig.md">WdfDeviceInitSetFileObjectConfig</a>.</p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>