---
UID: NF:wdfdevice.WdfDeviceSetDeviceInterfaceState
title: WdfDeviceSetDeviceInterfaceState function
author: windows-driver-content
description: The WdfDeviceSetDeviceInterfaceState method enables or disables a device interface for a specified device.
old-location: wdf\wdfdevicesetdeviceinterfacestate.htm
old-project: wdf
ms.assetid: 345003fc-fdc3-4529-bb15-c9e380e77bba
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DFDeviceObjectGeneralRef_bfed99aa-ad4c-4339-aeb9-f7d73039f0b9.xml, WdfDeviceSetDeviceInterfaceState, WdfDeviceSetDeviceInterfaceState method, kmdf.wdfdevicesetdeviceinterfacestate, wdf.wdfdevicesetdeviceinterfacestate, wdfdevice/WdfDeviceSetDeviceInterfaceState
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
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Wdf01000.sys
-	Wdf01000.sys.dll
-	WUDFx02000.dll
-	WUDFx02000.dll.dll
api_name:
-	WdfDeviceSetDeviceInterfaceState
product: Windows
targetos: Windows
req.typenames: WDF_STATE_NOTIFICATION_TYPE
req.product: Windows 10 or later.
---


# WdfDeviceSetDeviceInterfaceState function
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfDeviceSetDeviceInterfaceState</b> method enables or disables a device interface for a specified device.

## Syntax

```
void WdfDeviceSetDeviceInterfaceState(
  WDFDEVICE        Device,
  CONST GUID       *InterfaceClassGUID,
  PCUNICODE_STRING ReferenceString,
  BOOLEAN          IsInterfaceEnabled
);
```

## Parameters

`Device`

A handle to a framework device object.

`InterfaceClassGUID`

A pointer to a GUID that identifies the device interface class.

`ReferenceString`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure that describes a reference string for the device interface. This parameter is optional and can be <b>NULL</b>.

`IsInterfaceEnabled`

A Boolean value that, if <b>TRUE</b>, enables the specified device interface instance or, if <b>FALSE</b>, disables it.


## Return Value

None.

A bug check occurs if the driver supplies an invalid object handle.

## Remarks

For more information about device interfaces and the <b>WdfDeviceSetDeviceInterfaceState</b> method, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/using-device-interfaces">Using Device Interfaces</a>.


#### Examples

The following code example disables a driver's COM port interface.

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>WdfDeviceSetDeviceInterfaceState (
                                  Device,
                                  (LPGUID) &amp;GUID_DEVINTERFACE_COMPORT,
                                  NULL,
                                  FALSE
                                  );</pre>
</td>
</tr>
</table></span></div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfdevice.h (include Wdf.h) |
| **Library** | Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF) |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** | DriverCreate, KmdfIrql, KmdfIrql2 |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff545935">WdfDeviceCreateDeviceInterface</a>