---
UID: NE:hidpi._HIDP_REPORT_TYPE
title: "_HIDP_REPORT_TYPE"
author: windows-driver-content
description: The HIDP_REPORT_TYPE enumeration type is used to specify a HID report type.
old-location: hid\hidp_report_type.htm
old-project: hid
ms.assetid: adb2f0cc-f261-41d2-b30f-58286b351e4f
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: HIDP_REPORT_TYPE, HIDP_REPORT_TYPE enumeration [Human Input Devices], HidP_Feature, HidP_Input, HidP_Output, _HIDP_REPORT_TYPE, hid.hidp_report_type, hidpi/HIDP_REPORT_TYPE, hidpi/HidP_Feature, hidpi/HidP_Input, hidpi/HidP_Output, hidstrct_d25e996c-d904-410c-bacb-a79f17fad916.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: hidpi.h
req.include-header: Hidpi.h
req.target-type: Windows
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
req.lib: 
req.dll: 
req.irql: "<= DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	hidpi.h
api_name:
-	HIDP_REPORT_TYPE
product:
- Windows
targetos: Windows
req.typenames: HIDP_REPORT_TYPE
---

# _HIDP_REPORT_TYPE Enumeration
The HIDP_REPORT_TYPE enumeration type is used to specify a HID report type.

## Syntax
```
typedef enum _HIDP_REPORT_TYPE {
  HidP_Input    ,
  HidP_Output   ,
  HidP_Feature
} HIDP_REPORT_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>HidP_Input</td>
                    <td>Indicates an input report.</td>
                </tr>
            
                <tr>
                    <td>HidP_Output</td>
                    <td>Indicates an output report.</td>
                </tr>
            
                <tr>
                    <td>HidP_Feature</td>
                    <td>Indicates a feature report.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | hidpi.h (include Hidpi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff539693">HIDP_BUTTON_CAPS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539832">HIDP_VALUE_CAPS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539718">HidP_GetData</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff539783">HidP_SetData</a>