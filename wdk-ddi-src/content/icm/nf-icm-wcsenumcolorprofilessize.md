---
UID: NF:icm.WcsEnumColorProfilesSize
title: WcsEnumColorProfilesSize function
author: windows-driver-content
description: The WcsEnumColorProfilesSize function returns the size, in bytes, of the buffer required by the WcsEnumColorProfiles function to enumerate color profiles.
old-location: print\wcsenumcolorprofilessize.htm
old-project: print
ms.assetid: bcd9c781-aa44-4e90-9290-c9f13b192cae
ms.author: windowsdriverdev
ms.date: 4/20/2018
ms.keywords: WcsEnumColorProfilesSize, WcsEnumColorProfilesSize function [Print Devices], colorfnc_dec9b73e-e492-4fed-841f-bbc0c8a5f225.xml, icm/WcsEnumColorProfilesSize, print.wcsenumcolorprofilessize
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
-   APIRef
-   kbSyntax
api_type:
-   DllExport
api_location:
-   Mscms.dll
api_name:
-   WcsEnumColorProfilesSize
product:
- Windows
targetos: Windows
req.typenames: 
---

# WcsEnumColorProfilesSize function


## -description


The <code>WcsEnumColorProfilesSize</code> function returns the size, in bytes, of the buffer required by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563720">WcsEnumColorProfiles</a> function to enumerate color profiles.


## -parameters




### -param scope




### -param pEnumRecord [in]

A pointer to a structure that specifies the enumeration criteria.


### -param pdwSize [out]

A pointer to a variable that receives the size of the buffer that is required to receive all enumerated profile names. This value is used by the <i>dwSize</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563720">WcsEnumColorProfiles</a> function.


#### - profileManagementScope [in]

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff563752">WCS_PROFILE_MANAGEMENT_SCOPE</a> value that specifies the scope of the profile management operation performed by this function.


## -remarks



This function is executable in Least-Privileged User Account (LUA) context.




## -see-also




<a href="https://msdn.microsoft.com/library/windows/hardware/ff563752">WCS_PROFILE_MANAGEMENT_SCOPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff563720">WcsEnumColorProfiles</a>
�

�

