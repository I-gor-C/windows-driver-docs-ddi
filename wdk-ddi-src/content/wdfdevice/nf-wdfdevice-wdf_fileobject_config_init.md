---
UID: NF.wdfdevice.WDF_FILEOBJECT_CONFIG_INIT
title: WDF_FILEOBJECT_CONFIG_INIT function
author: windows-driver-content
description: The WDF_FILEOBJECT_CONFIG_INIT function initializes a driver's WDF_FILEOBJECT_CONFIG structure.
old-location: wdf\wdf_fileobject_config_init.htm
old-project: wdf
ms.assetid: 87ad817a-4a62-4061-949c-fe45bdfb44d5
ms.author: windowsdriverdev
ms.date: 12/7/2017
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
req.product: Windows 10 or later.
---

# WDF_FILEOBJECT_CONFIG_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_FILEOBJECT_CONFIG_INIT</b> function initializes a driver's <a href="wdf.wdf_fileobject_config">WDF_FILEOBJECT_CONFIG</a> structure.



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

### -param FileEventCallbacks [out]

A pointer to a driver-allocated <a href="wdf.wdf_fileobject_config">WDF_FILEOBJECT_CONFIG</a> structure.


### -param EvtDeviceFileCreate [in, optional]

A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt_wdf_device_file_create.md">EvtDeviceFileCreate</a> event callback function.


### -param EvtFileClose [in, optional]

A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt_wdf_file_close.md">EvtFileClose</a> event callback function.


### -param EvtFileCleanup [in, optional]

A pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt_wdf_file_cleanup.md">EvtFileCleanup</a> event callback function.


## -returns
None


## -remarks
The <b>WDF_FILEOBJECT_CONFIG_INIT</b> function sets the specified <a href="wdf.wdf_fileobject_config">WDF_FILEOBJECT_CONFIG</a> structure's <b>Size</b> member, stores the specified callback function pointers, sets the <b>FileObjectClass</b> member to <b>WdfFileObjectWdfCannotUseFsContexts</b>, and sets the <b>AutoForwardCleanupClose</b> member to <b>WdfUseDefault</b>. 

For a code example that uses <b>WDF_FILEOBJECT_CONFIG_INIT</b>, see <a href="wdf.wdfdeviceinitsetfileobjectconfig">WdfDeviceInitSetFileObjectConfig</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
</table>