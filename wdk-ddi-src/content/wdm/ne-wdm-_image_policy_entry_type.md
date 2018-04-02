---
UID: NE:wdm._IMAGE_POLICY_ENTRY_TYPE
title: "_IMAGE_POLICY_ENTRY_TYPE"
author: windows-driver-content
description: This enumeration is not supported.
old-location: kernel\_image_policy_entry_type.htm
old-project: kernel
ms.assetid: f8ce3297-5a57-4ece-a74c-ae5e4e15ce3e
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: IMAGE_POLICY_ENTRY_TYPE, IMAGE_POLICY_ENTRY_TYPE enumeration [Kernel-Mode Driver Architecture], ImagePolicyEntryTypeAnsiString, ImagePolicyEntryTypeBool, ImagePolicyEntryTypeInt16, ImagePolicyEntryTypeInt32, ImagePolicyEntryTypeInt64, ImagePolicyEntryTypeInt8, ImagePolicyEntryTypeMaximum, ImagePolicyEntryTypeUInt16, ImagePolicyEntryTypeUInt32, ImagePolicyEntryTypeUInt64, ImagePolicyEntryTypeUInt8, ImagePolicyEntryTypeUnicodeString, _IMAGE_POLICY_ENTRY_TYPE, kernel._image_policy_entry_type, wdm/IMAGE_POLICY_ENTRY_TYPE, wdm/ImagePolicyEntryTypeAnsiString, wdm/ImagePolicyEntryTypeBool, wdm/ImagePolicyEntryTypeInt16, wdm/ImagePolicyEntryTypeInt32, wdm/ImagePolicyEntryTypeInt64, wdm/ImagePolicyEntryTypeInt8, wdm/ImagePolicyEntryTypeMaximum, wdm/ImagePolicyEntryTypeUInt16, wdm/ImagePolicyEntryTypeUInt32, wdm/ImagePolicyEntryTypeUInt64, wdm/ImagePolicyEntryTypeUInt8, wdm/ImagePolicyEntryTypeUnicodeString
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wdm.h
api_name:
-	IMAGE_POLICY_ENTRY_TYPE
product: Windows
targetos: Windows
req.typenames: IMAGE_POLICY_ENTRY_TYPE
req.product: Windows 10 or later.
---

# _IMAGE_POLICY_ENTRY_TYPE Enumeration
This enumeration is not supported.

## Syntax
```
typedef enum _IMAGE_POLICY_ENTRY_TYPE {
  ImagePolicyEntryTypeNone           ,
  ImagePolicyEntryTypeBool           ,
  ImagePolicyEntryTypeInt8           ,
  ImagePolicyEntryTypeUInt8          ,
  ImagePolicyEntryTypeInt16          ,
  ImagePolicyEntryTypeUInt16         ,
  ImagePolicyEntryTypeInt32          ,
  ImagePolicyEntryTypeUInt32         ,
  ImagePolicyEntryTypeInt64          ,
  ImagePolicyEntryTypeUInt64         ,
  ImagePolicyEntryTypeAnsiString     ,
  ImagePolicyEntryTypeUnicodeString  ,
  ImagePolicyEntryTypeMaximum
} IMAGE_POLICY_ENTRY_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>ImagePolicyEntryTypeNone</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>ImagePolicyEntryTypeBool</td>
                    <td>Reserved.</td>
                </tr>
            
                <tr>
                    <td>ImagePolicyEntryTypeInt8</td>
                    <td>Reserved.</td>
                </tr>
            
                <tr>
                    <td>ImagePolicyEntryTypeUInt8</td>
                    <td>Reserved.</td>
                </tr>
            
                <tr>
                    <td>ImagePolicyEntryTypeInt16</td>
                    <td>Reserved.</td>
                </tr>
            
                <tr>
                    <td>ImagePolicyEntryTypeUInt16</td>
                    <td>Reserved.</td>
                </tr>
            
                <tr>
                    <td>ImagePolicyEntryTypeInt32</td>
                    <td>Reserved.</td>
                </tr>
            
                <tr>
                    <td>ImagePolicyEntryTypeUInt32</td>
                    <td>Reserved.</td>
                </tr>
            
                <tr>
                    <td>ImagePolicyEntryTypeInt64</td>
                    <td>Reserved.</td>
                </tr>
            
                <tr>
                    <td>ImagePolicyEntryTypeUInt64</td>
                    <td>Reserved.</td>
                </tr>
            
                <tr>
                    <td>ImagePolicyEntryTypeAnsiString</td>
                    <td>Reserved.</td>
                </tr>
            
                <tr>
                    <td>ImagePolicyEntryTypeUnicodeString</td>
                    <td>Reserved.</td>
                </tr>
            
                <tr>
                    <td>ImagePolicyEntryTypeMaximum</td>
                    <td>Reserved.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h) |