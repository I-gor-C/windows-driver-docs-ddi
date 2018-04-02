---
UID: NF:icm.WcsGetUsePerUserProfiles
title: WcsGetUsePerUserProfiles function
author: windows-driver-content
description: The WcsGetUsePerUserProfiles function determines whether the user has chosen to use a per-user profile association list for the specified device.
old-location: print\wcsgetuseperuserprofiles.htm
old-project: print
ms.assetid: 6a970bec-c773-498e-b93a-2bd9f625e194
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: WcsGetUsePerUserProfiles, WcsGetUsePerUserProfiles function [Print Devices], colorfnc_b80783e5-17c0-4069-90ba-71ea82a2d7d5.xml, icm/WcsGetUsePerUserProfiles, print.wcsgetuseperuserprofiles
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: icm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Included in Windows Vista and later.
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
req.lib: Mscms.lib
req.dll: Mscms.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	Mscms.dll
api_name:
-	WcsGetUsePerUserProfiles
product:
- Windows
targetos: Windows
req.typenames: WCS_PROFILE_MANAGEMENT_SCOPE
---


# WcsGetUsePerUserProfiles function
The <code>WcsGetUsePerUserProfiles</code> function determines whether the user has chosen to use a per-user profile association list for the specified device.

## Syntax

```
BOOL WcsGetUsePerUserProfiles(
  LPCWSTR pDeviceName,
  DWORD   dwDeviceClass,
  PBOOL   pUsePerUserProfiles
);
```

## Parameters

`pDeviceName`

A pointer to a string that contains the friendly name of the device.

`dwDeviceClass`

A flag value that specifies the class of the device. This parameter must take one of the following values:





#### CLASS_MONITOR

Specifies a display device.



#### CLASS_PRINTER

Specifies a printer.



#### CLASS_SCANNER

Specifies an image capture device.

`pUsePerUserProfiles`

A pointer to a location to receive a Boolean value that is <b>TRUE</b> if the user has chosen to use a per-user profile association list for the specified device; otherwise <b>FALSE</b>.


## Return Value

None

## Remarks

This function will fail if the device pointed to by <i>pDeviceName</i> is not of the class specified by <i>dwDeviceClass</i>.

This function is executable in Least-Privileged User Account (LUA) context.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Included in Windows Vista and later.  |
| **Target Platform** | Universal |
| **Header** | icm.h |
| **Library** | Mscms.lib |
| **DLL** | Mscms.dll |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff563741">WcsSetUsePerUserProfiles</a>