---
UID: NE:wdfobject._WDF_EXECUTION_LEVEL
title: "_WDF_EXECUTION_LEVEL"
author: windows-driver-content
description: The WDF_EXECUTION_LEVEL enumeration type specifies the maximum IRQL at which the framework will call the event callback functions that a driver has supplied for a framework object.
old-location: wdf\wdf_execution_level.htm
old-project: wdf
ms.assetid: 82b1fe8e-054c-4710-9a32-d620a62a070e
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DFGenObjectRef_f9a9ae20-9dba-4c23-910b-04c60e1f9539.xml, WDF_EXECUTION_LEVEL, WDF_EXECUTION_LEVEL enumeration, WdfExecutionLevelDispatch, WdfExecutionLevelInheritFromParent, WdfExecutionLevelInvalid, WdfExecutionLevelPassive, _WDF_EXECUTION_LEVEL, kmdf.wdf_execution_level, wdf.wdf_execution_level, wdfobject/WDF_EXECUTION_LEVEL, wdfobject/WdfExecutionLevelDispatch, wdfobject/WdfExecutionLevelInheritFromParent, wdfobject/WdfExecutionLevelInvalid, wdfobject/WdfExecutionLevelPassive
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfobject.h
req.include-header: Wdf.h
req.target-type: Windows
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
req.lib: 
req.dll: 
req.irql: See Remarks section.
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wdfobject.h
api_name:
-	WDF_EXECUTION_LEVEL
product:
- Windows
targetos: Windows
req.typenames: WDF_EXECUTION_LEVEL
req.product: Windows 10 or later.
---

# _WDF_EXECUTION_LEVEL Enumeration
<p class="CCE_Message">[Applies to KMDF and UMDF]

The WDF_EXECUTION_LEVEL enumeration type specifies the maximum IRQL at which the framework will call the event callback functions that a driver has supplied for a framework object.

## Syntax
```
typedef enum _WDF_EXECUTION_LEVEL {
  WdfExecutionLevelInvalid            ,
  WdfExecutionLevelInheritFromParent  ,
  WdfExecutionLevelPassive            ,
  WdfExecutionLevelDispatch
} WDF_EXECUTION_LEVEL;
```

## Constants

<table>
            
                <tr>
                    <td>WdfExecutionLevelInvalid</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>WdfExecutionLevelInheritFromParent</td>
                    <td>The framework uses the maximum IRQL value of the object's parent, unless the object is one that requires IRQL = DISPATCH_LEVEL (such as a DPC object). This value is the default if a driver does not specify a WDF_EXECUTION_LEVEL-typed value.</td>
                </tr>
            
                <tr>
                    <td>WdfExecutionLevelPassive</td>
                    <td>The framework always calls the object's callback functions at IRQL = PASSIVE_LEVEL.</td>
                </tr>
            
                <tr>
                    <td>WdfExecutionLevelDispatch</td>
                    <td>The framework calls the object's callback functions at IRQL &lt;= DISPATCH_LEVEL. Not available in UMDF.</td>
                </tr>
</table>

## Remarks

Drivers use the WDF_EXECUTION_LEVEL enumeration type to specify the <b>ExecutionLevel</b> member of an object's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure.

You can specify an <b>ExecutionLevel</b> value for the following objects:

<ul>
<li>
Framework driver objects

</li>
<li>
Framework device objects

</li>
<li>
Framework file objects

</li>
<li>
Framework general objects

</li>
<li>
Framework queue objects (Framework versions 1.9 and later)

</li>
<li>
Framework timer objects (Framework versions 1.9 and later)

</li>
</ul>
<b>KMDF </b>By default, the framework sets the <b>ExecutionLevel</b> value of framework driver objects to <b>WdfExecutionLevelDispatch.</b>

<b>UMDF </b>By default, the framework sets the <b>ExecutionLevel</b> value of framework driver objects to <b>WdfExecutionLevelPassive.</b>

The default <b>ExecutionLevel</b> value for all other objects is <b>WdfExecutionLevelInheritFromParent.</b>

For more information about execution levels for event callback functions, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/synchronization-techniques-for-wdf-drivers">Synchronization Techniques for Framework-Based Drivers</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfobject.h (include Wdf.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a>