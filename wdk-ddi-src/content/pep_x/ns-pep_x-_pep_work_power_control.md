---
UID: NS:pep_x._PEP_WORK_POWER_CONTROL
title: "_PEP_WORK_POWER_CONTROL"
author: windows-driver-content
description: The PEP_WORK_POWER_CONTROL structure contains the parameters for a power control request that the platform extension plug-in (PEP) sends directly to a processor driver.
old-location: kernel\pep_work_power_control.htm
old-project: kernel
ms.assetid: 84258422-A2AE-449F-97C8-41336FEA5D8B
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PPEP_WORK_POWER_CONTROL, PEP_WORK_POWER_CONTROL, PEP_WORK_POWER_CONTROL structure [Kernel-Mode Driver Architecture], PPEP_WORK_POWER_CONTROL, PPEP_WORK_POWER_CONTROL structure pointer [Kernel-Mode Driver Architecture], _PEP_WORK_POWER_CONTROL, kernel.pep_work_power_control, pepfx/PEP_WORK_POWER_CONTROL, pepfx/PPEP_WORK_POWER_CONTROL"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pep_x.h
req.include-header: Pep_x.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
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
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	pepfx.h
api_name:
-	PEP_WORK_POWER_CONTROL
product: Windows
targetos: Windows
req.typenames: PEP_WORK_POWER_CONTROL, *PPEP_WORK_POWER_CONTROL, PEP_WORK_POWER_CONTROL, *PPEP_WORK_POWER_CONTROL
---

# _PEP_WORK_POWER_CONTROL structure
The <b>PEP_WORK_POWER_CONTROL</b> structure contains the parameters for a <a href="https://msdn.microsoft.com/10A30691-CDF9-4B62-B6E8-790CA52C0E91">power control request</a> that the platform extension plug-in (PEP) sends directly to a processor driver.

## Syntax
```
typedef struct _PEP_WORK_POWER_CONTROL {
  POHANDLE DeviceHandle;
  LPCGUID  PowerControlCode;
  PVOID    RequestContext;
  PVOID    InBuffer;
  SIZE_T   InBufferSize;
  PVOID    OutBuffer;
  SIZE_T   OutBufferSize;
} PEP_WORK_POWER_CONTROL, *PPEP_WORK_POWER_CONTROL;
```

## Members


`DeviceHandle`

A POHANDLE value that identifies the processor. The PEP received this handle in a previous <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186849">PEP_DPM_REGISTER_DEVICE</a> notification.

`PowerControlCode`

[in] A pointer to a <a href="http://msdn.microsoft.com/library/windows/desktop/aa373931(v=vs.85).aspx">GUID</a> value that specifies the power control operation to perform.

`RequestContext`

A pointer to a PEP-defined context value. The PEP might use this value to uniquely identify a power control request message (in case the PEP issues multiple requests with the same control code to the same device).

`InBuffer`

[in] A pointer to a driver-allocated input buffer that contains the input parameters for this power control operation.

`InBufferSize`

[in] The size in bytes of the buffer pointed to by <b>InBuffer</b>.

`OutBuffer`

[in] A pointer to a driver-allocated output buffer to which the PEP writes the results of this power control operation.

`OutBufferSize`

[in] The size in bytes of the buffer pointed to by <b>OutBuffer</b>.

## Remarks
The <b>PowerControl</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt186864">PEP_WORK_INFORMATION</a> structure is a pointer to a <b>PEP_WORK_POWER_CONTROL</b> structure.

The PEP issues a power control request from a worker thread. The Windows <a href="https://msdn.microsoft.com/B08F8ABF-FD43-434C-A345-337FBB799D9B">power management framework</a> (PoFx) forwards this request by calling the processor driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh439564">PowerControlCallback</a> routine, if the driver implements this routine.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10. Supported starting with Windows 10. |
| **Header** | pep_x.h (include Pep_x.h) |

## See Also

<a href="http://msdn.microsoft.com/library/windows/desktop/aa373931(v=vs.85).aspx">GUID</a>



<a href="https://msdn.microsoft.com/en-us/library/windows/hardware/mt186849">PEP_DPM_REGISTER_DEVICE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt186864">PEP_WORK_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439521">PoFxRegisterDevice</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh439564">PowerControlCallback</a>