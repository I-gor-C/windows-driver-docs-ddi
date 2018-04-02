---
UID: NF:wdfobject.WdfObjectContextGetObject
title: WdfObjectContextGetObject function
author: windows-driver-content
description: The WdfObjectContextGetObject method returns a handle to the framework object that a specified context space belongs to.
old-location: wdf\wdfobjectcontextgetobject.htm
old-project: wdf
ms.assetid: 7288a7e5-8e64-4ac3-9779-edc27a3888bb
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DFGenObjectRef_cf11ce54-dbb0-4835-919d-6f0bec903e2d.xml, WdfObjectContextGetObject, WdfObjectContextGetObject method, kmdf.wdfobjectcontextgetobject, wdf.wdfobjectcontextgetobject, wdfobject/WdfObjectContextGetObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfobject.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: Any level
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
-	WdfObjectContextGetObject
product: Windows
targetos: Windows
req.typenames: WDF_SYNCHRONIZATION_SCOPE
req.product: Windows 10 or later.
---


# WdfObjectContextGetObject function
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfObjectContextGetObject</b> method returns a handle to the framework object that a specified context space belongs to.

## Syntax

```
WDFOBJECT WdfObjectContextGetObject(
  PVOID ContextPointer
);
```

## Parameters

`ContextPointer`

A pointer to object context space. The driver can obtain this pointer by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548749">WdfObjectGetTypedContext</a>.


## Return Value

<b>WdfObjectContextGetObject</b> returns a handle to a framework object.

## Remarks

For more information about object context space, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/framework-object-context-space">Framework Object Context Space</a>. 


#### Examples

The following code example obtains a handle to the framework object that a specified context space belongs to.

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>WDFDEVICE  device;

device = WdfObjectContextGetObject(DeviceContext);</pre>
</td>
</tr>
</table></span></div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfobject.h (include Wdf.h) |
| **Library** | Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF) |
| **IRQL** | Any level |
| **DDI compliance rules** | DriverCreate |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff548749">WdfObjectGetTypedContext</a>