---
UID: NE:d3dkmthk._D3DKMT_SCHEDULINGPRIORITYCLASS
title: "_D3DKMT_SCHEDULINGPRIORITYCLASS"
author: windows-driver-content
description: The D3DKMT_SCHEDULINGPRIORITYCLASS enumeration type contains values that describe the scheduling priority for a process.
old-location: display\d3dkmt_schedulingpriorityclass.htm
old-project: display
ms.assetid: d42e37d0-0ba9-4b79-903d-fdbb478ab196
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMT_SCHEDULINGPRIORITYCLASS, D3DKMT_SCHEDULINGPRIORITYCLASS enumeration [Display Devices], D3DKMT_SCHEDULINGPRIORITYCLASS_ABOVE_NORMAL, D3DKMT_SCHEDULINGPRIORITYCLASS_BELOW_NORMAL, D3DKMT_SCHEDULINGPRIORITYCLASS_HIGH, D3DKMT_SCHEDULINGPRIORITYCLASS_IDLE, D3DKMT_SCHEDULINGPRIORITYCLASS_NORMAL, D3DKMT_SCHEDULINGPRIORITYCLASS_REALTIME, OpenGL_Structs_4e331f58-8ed5-4aff-ac73-5af374f0d556.xml, _D3DKMT_SCHEDULINGPRIORITYCLASS, d3dkmthk/D3DKMT_SCHEDULINGPRIORITYCLASS, d3dkmthk/D3DKMT_SCHEDULINGPRIORITYCLASS_ABOVE_NORMAL, d3dkmthk/D3DKMT_SCHEDULINGPRIORITYCLASS_BELOW_NORMAL, d3dkmthk/D3DKMT_SCHEDULINGPRIORITYCLASS_HIGH, d3dkmthk/D3DKMT_SCHEDULINGPRIORITYCLASS_IDLE, d3dkmthk/D3DKMT_SCHEDULINGPRIORITYCLASS_NORMAL, d3dkmthk/D3DKMT_SCHEDULINGPRIORITYCLASS_REALTIME, display.d3dkmt_schedulingpriorityclass
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmthk.h
api_name:
-	D3DKMT_SCHEDULINGPRIORITYCLASS
product: Windows
targetos: Windows
req.typenames: D3DKMT_SCHEDULINGPRIORITYCLASS
---

# _D3DKMT_SCHEDULINGPRIORITYCLASS Enumeration
The D3DKMT_SCHEDULINGPRIORITYCLASS enumeration type contains values that describe the scheduling priority for a process.

## Syntax
```
typedef enum _D3DKMT_SCHEDULINGPRIORITYCLASS {
  D3DKMT_SCHEDULINGPRIORITYCLASS_IDLE          ,
  D3DKMT_SCHEDULINGPRIORITYCLASS_BELOW_NORMAL  ,
  D3DKMT_SCHEDULINGPRIORITYCLASS_NORMAL        ,
  D3DKMT_SCHEDULINGPRIORITYCLASS_ABOVE_NORMAL  ,
  D3DKMT_SCHEDULINGPRIORITYCLASS_HIGH          ,
  D3DKMT_SCHEDULINGPRIORITYCLASS_REALTIME
} D3DKMT_SCHEDULINGPRIORITYCLASS;
```

## Constants

<table>
            
                <tr>
                    <td>D3DKMT_SCHEDULINGPRIORITYCLASS_IDLE</td>
                    <td>The process is idle.</td>
                </tr>
            
                <tr>
                    <td>D3DKMT_SCHEDULINGPRIORITYCLASS_BELOW_NORMAL</td>
                    <td>The scheduling priority of the process is below normal.</td>
                </tr>
            
                <tr>
                    <td>D3DKMT_SCHEDULINGPRIORITYCLASS_NORMAL</td>
                    <td>The scheduling priority of the process is normal.</td>
                </tr>
            
                <tr>
                    <td>D3DKMT_SCHEDULINGPRIORITYCLASS_ABOVE_NORMAL</td>
                    <td>The scheduling priority of the process is above normal.</td>
                </tr>
            
                <tr>
                    <td>D3DKMT_SCHEDULINGPRIORITYCLASS_HIGH</td>
                    <td>The scheduling priority of the process is high.</td>
                </tr>
            
                <tr>
                    <td>D3DKMT_SCHEDULINGPRIORITYCLASS_REALTIME</td>
                    <td>The scheduling priority of the process is in real time.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546992">D3DKMTGetProcessSchedulingPriorityClass</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff547182">D3DKMTSetProcessSchedulingPriorityClass</a>