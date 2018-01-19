---
UID : NF:storport.StorPortInitialize
title : StorPortInitialize function
author : windows-driver-content
description : The StorPortInitilize routine initializes the port driver parameters and extension data. StorPortInitilize also saves the adapter information provided from the miniport driver.
old-location : storage\storportinitialize.htm
old-project : storage
ms.assetid : b560ce42-3c5c-4766-bb9c-6590b7113ecd
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : StorPortInitialize
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : storport.h
req.include-header : Storport.h
req.target-type : Universal
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : StorPortInitialize
req.alt-loc : Storport.lib,Storport.dll
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Storport.lib
req.dll : 
req.irql : 
req.typenames : STOR_SPINLOCK
req.product : Windows 10 or later.
---


# StorPortInitialize function
The <b>StorPortInitilize</b> routine initializes the port  driver parameters and extension data. <b>StorPortInitilize</b> also saves the adapter information provided from the miniport driver.

## Syntax

````
STORPORT_API ULONG StorPortInitialize(
  _In_     PVOID                   Argument1,
  _In_     PVOID                   Argument2,
  _In_     PHW_INITIALIZATION_DATA HwInitializationData,
  _In_opt_ PVOID                   HwContext
);
````

## Parameters

`Argument1`

The first pointer with which the operating system called the miniport's <a href="..\wdm\nc-wdm-driver_initialize.md">DriverEntry</a> routine.

`Argument2`

The second pointer with which the operating system called the miniports's <a href="..\wdm\nc-wdm-driver_initialize.md">DriverEntry</a> routine.

`HwInitializationData`

Pointer to the initialization and configuration information set by the miniport driver in it's <a href="..\wdm\nc-wdm-driver_initialize.md">DriverEntry</a> routine.

`HwContext`

Is the address of a context value to be passed to the miniport driver's <a href="..\storport\nc-storport-hw_find_adapter.md">HwStorFindAdapter</a> routine. Only legacy miniport drivers that scan the bus for HBAs rather than receiving configuration information from the port driver can use this parameter to store state between calls to <b>HwStorFindAdapter</b>.


## Return Value

The result of the initialization actions performed by <b>StorPortInitilize</b>. The miniport driver will return this value as the return value for its <a href="..\wdm\nc-wdm-driver_initialize.md">DriverEntry</a> routine.

<b>StorPortInitilize</b> returns one of the following status codes:
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><i>Argument1</i> is NULL.

-or-

<i>Argument2</i> is NULL.

-or-

<i>HwInitializationData</i> is NULL.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The driver extension data and adapter information were initialized successfully.
<dl>
<dt><b> STATUS_NO_MEMORY</b></dt>
</dl>No memory is available to store an initialization parameter.
<dl>
<dt><b> STATUS_REVISION_MISMATCH</b></dt>
</dl>The version of the structure pointed to by <i>HwInitializationData</i> is invalid for the current operating system.
<dl>
<dt><b> STATUS_INSUFFICENT_RESOURCES</b></dt>
</dl>The allocation failed for the driver object extension data.

## Remarks

This routine must be called from the miniport driver's <a href="..\wdm\nc-wdm-driver_initialize.md">DriverEntry</a> routine.

Because Storport miniport drivers must support PnP, the Storport driver does not use the <i>HwContext</i> parameter passed to <b>StorPortInitilize</b>.

Every miniport driver's <a href="..\wdm\nc-wdm-driver_initialize.md">DriverEntry</a> routine must call <b>StorPortInitilize</b> after the miniport driver has first zeroed and then set the members of <a href="..\storport\ns-storport-_hw_initialization_data.md">HW_INITIALIZATION_DATA</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | storport.h (include Storport.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\storport\ns-storport-_hw_initialization_data.md">HW_INITIALIZATION_DATA</a>
</dt>
<dt>
<a href="..\storport\nc-storport-hw_find_adapter.md">HwStorFindAdapter</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortInitialize routine%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>