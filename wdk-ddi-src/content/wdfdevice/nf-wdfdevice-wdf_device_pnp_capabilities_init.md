---
UID: NF:wdfdevice.WDF_DEVICE_PNP_CAPABILITIES_INIT
title: WDF_DEVICE_PNP_CAPABILITIES_INIT function
author: windows-driver-content
description: The WDF_DEVICE_PNP_CAPABILITIES_INIT function initializes a WDF_DEVICE_PNP_CAPABILITIES structure.
old-location: wdf\wdf_device_pnp_capabilities_init.htm
old-project: wdf
ms.assetid: 5ae60715-ba51-4814-ae34-34967cdbab78
ms.author: windowsdriverdev
ms.date: 1/11/2018
ms.keywords: wdf.wdf_device_pnp_capabilities_init, WDF_DEVICE_PNP_CAPABILITIES_INIT function, kmdf.wdf_device_pnp_capabilities_init, wdfdevice/WDF_DEVICE_PNP_CAPABILITIES_INIT, WDF_DEVICE_PNP_CAPABILITIES_INIT, DFDeviceObjectGeneralRef_630e05dc-1566-4dc4-b35c-d9b756629c99.xml
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.exe
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	wdfdevice.h
apiname:
-	WDF_DEVICE_PNP_CAPABILITIES_INIT
product: Windows
targetos: Windows
req.typenames: WDF_STATE_NOTIFICATION_TYPE
req.product: Windows 10 or later.
---


# WDF_DEVICE_PNP_CAPABILITIES_INIT function
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_DEVICE_PNP_CAPABILITIES_INIT</b> function initializes a <a href="..\wdfdevice\ns-wdfdevice-_wdf_device_pnp_capabilities.md">WDF_DEVICE_PNP_CAPABILITIES</a> structure.

## Syntax

````
VOID WDF_DEVICE_PNP_CAPABILITIES_INIT(
  _Out_ PWDF_DEVICE_PNP_CAPABILITIES Caps
);
````

## Parameters

`Caps`

A pointer to a driver-supplied <a href="..\wdfdevice\ns-wdfdevice-_wdf_device_pnp_capabilities.md">WDF_DEVICE_PNP_CAPABILITIES</a> structure.


## Return Value

None

## Remarks

The <b>WDF_DEVICE_PNP_CAPABILITIES_INIT</b> function zeros the specified <a href="..\wdfdevice\ns-wdfdevice-_wdf_device_pnp_capabilities.md">WDF_DEVICE_PNP_CAPABILITIES</a> structure, sets the structure's <b>Size</b> member, and sets other members to default values.


#### Examples

For a code example that uses <b>WDF_DEVICE_PNP_CAPABILITIES_INIT</b>, see <a href="..\wdfdevice\nf-wdfdevice-wdfdevicesetpnpcapabilities.md">WdfDeviceSetPnpCapabilities</a>.

<div class="code"></div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfdevice.h (include Wdf.h) |
| **Library** | NtosKrnl.exe |