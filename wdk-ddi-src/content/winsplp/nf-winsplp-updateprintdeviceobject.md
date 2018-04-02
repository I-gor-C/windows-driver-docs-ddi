---
UID: NF:winsplp.UpdatePrintDeviceObject
title: UpdatePrintDeviceObject function
author: windows-driver-content
description: The UpdatePrintDeviceObject function updates the properties of a device object that is in the print provider queue.
old-location: print\updateprintdeviceobject.htm
old-project: print
ms.assetid: 52E8F8BF-0362-4BA9-BABD-7B009B3FFA7F
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: UpdatePrintDeviceObject, UpdatePrintDeviceObject function [Print Devices], print.updateprintdeviceobject, winsplp/UpdatePrintDeviceObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: winsplp.h
req.include-header: Winspool.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: WinSpool.lib
req.dll: WinSpool.drv
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	WinSpool.drv
api_name:
-	UpdatePrintDeviceObject
product: Windows
targetos: Windows
req.typenames: NOTIFICATION_CONFIG_FLAGS
req.product: Windows 10 or later.
---


# UpdatePrintDeviceObject function
<div class="alert"><b>Warning</b>  <p class="note">Starting with Windows 10, the APIs which support third-party print providers are deprecated. Microsoft does not recommend any investment into third-party print providers. Additionally, on Windows 8 and newer products where the v4 print driver model is available, third-party print providers may not create or manage queues which use v4 print drivers.

</div><div> </div>The <b>UpdatePrintDeviceObject</b> function updates the properties of a device object that is in the print provider queue.

## Syntax

```
HRESULT UpdatePrintDeviceObject(
  HANDLE hPrinter,
  HANDLE hDeviceObject
);
```

## Parameters

`hPrinter`

The HANDLE to an open printer. This should be a handle that was returned by the <b>AddPrinter</b> or <b>OpenPrinter</b> spooler functions.

`hDeviceObject`

The HANDLE to the device object to be updated. This should be a device object that was created with <a href="https://msdn.microsoft.com/library/windows/hardware/dn917890">AddPrintDeviceObject</a>.


## Return Value

The <b>UpdatePrintDeviceObject</b> function returns S_OK, if the properties of the  device object were updated successfully. Otherwise it returns an error.

For example, this function can return HRESULT_FROM_WIN32(ERROR_INVALID_HANDLE), if the function call was made with an invalid HANDLE, or the device object was removed before the function call was made.

## Remarks

The <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/dd162845(v=vs.85).aspx">PRINTER_INFO_2</a>  structure is a good example of the kind of properties that <b>UpdatePrintDeviceObject</b> can update.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | winsplp.h (include Winspool.h) |
| **Library** | WinSpool.lib |
| **DLL** | WinSpool.drv |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn917890">AddPrintDeviceObject</a>



<a href="http://msdn.microsoft.com/en-us/library/windows/desktop/dd162845(v=vs.85).aspx">PRINTER_INFO_2</a>