---
UID: NF:wdfdevice.WDF_DEVICE_STATE_INIT
title: WDF_DEVICE_STATE_INIT function
author: windows-driver-content
description: The WDF_DEVICE_STATE_INIT function initializes a driver's WDF_DEVICE_STATE structure.
old-location: wdf\wdf_device_state_init.htm
old-project: wdf
ms.assetid: f8c040aa-bfa0-4b74-ad0a-8796f1cfc4b8
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DFDeviceObjectGeneralRef_702c7f79-a50f-4115-ba93-82388ccbf063.xml, WDF_DEVICE_STATE_INIT, WDF_DEVICE_STATE_INIT function, kmdf.wdf_device_state_init, wdf.wdf_device_state_init, wdfdevice/WDF_DEVICE_STATE_INIT
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wdfdevice.h
api_name:
-	WDF_DEVICE_STATE_INIT
product: Windows
targetos: Windows
req.typenames: WDF_STATE_NOTIFICATION_TYPE
req.product: Windows 10 or later.
---


# WDF_DEVICE_STATE_INIT function
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_DEVICE_STATE_INIT</b> function initializes a driver's <a href="..\wdfdevice\ns-wdfdevice-_wdf_device_state.md">WDF_DEVICE_STATE</a> structure.

## Syntax

````
VOID WDF_DEVICE_STATE_INIT(
  _Out_ PWDF_DEVICE_STATE PnpDeviceState
);
````

## Parameters

`PnpDeviceState`

A pointer to a driver-allocated <a href="..\wdfdevice\ns-wdfdevice-_wdf_device_state.md">WDF_DEVICE_STATE</a> structure.


## Return Value

None

## Remarks

The <b>WDF_DEVICE_STATE_INIT</b> function initializes all of the <a href="..\wdfdevice\ns-wdfdevice-_wdf_device_state.md">WDF_DEVICE_STATE</a> structure's <a href="..\wudfddi_types\ne-wudfddi_types-_wdf_tri_state.md">WDF_TRI_STATE</a>-typed members to <b>WdfUseDefault</b>.


#### Examples

For a code example that uses <b>WDF_DEVICE_STATE_INIT</b>, see <a href="..\wdfdevice\nf-wdfdevice-wdfdevicesetdevicestate.md">WdfDeviceSetDeviceState</a>.

<div class="code"></div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfdevice.h (include Wdf.h) |
| **Library** | NtosKrnl.exe |

## See Also

<a href="..\wdfdevice\ns-wdfdevice-_wdf_device_state.md">WDF_DEVICE_STATE</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DEVICE_STATE_INIT function%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>