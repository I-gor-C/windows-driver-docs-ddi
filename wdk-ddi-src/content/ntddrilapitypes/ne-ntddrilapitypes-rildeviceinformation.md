---
UID: NE:ntddrilapitypes.RILDEVICEINFORMATION
title: RILDEVICEINFORMATION
author: windows-driver-content
description: This enumeration describes the RILDEVICEINFORMATION.
old-location: netvista\rildeviceinformation.htm
old-project: netvista
ms.assetid: 1abba51c-1db9-4424-aa11-64d3fd116a79
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: RILDEVICEINFORMATION, RILDEVICEINFORMATION enumeration [Network Drivers Starting with Windows Vista], RIL_DEVICEINFO_ARG_LARGEST, RIL_DEVICEINFO_ARG_SMALLEST, RIL_DEVICEINFO_MANUFACTURER, RIL_DEVICEINFO_MODEL, RIL_DEVICEINFO_REVISION, RIL_DEVICEINFO_SERIALNUMBER_CDMA, RIL_DEVICEINFO_SERIALNUMBER_GW, netvista.rildeviceinformation, rilapitypes/RILDEVICEINFORMATION, rilapitypes/RIL_DEVICEINFO_ARG_LARGEST, rilapitypes/RIL_DEVICEINFO_ARG_SMALLEST, rilapitypes/RIL_DEVICEINFO_MANUFACTURER, rilapitypes/RIL_DEVICEINFO_MODEL, rilapitypes/RIL_DEVICEINFO_REVISION, rilapitypes/RIL_DEVICEINFO_SERIALNUMBER_CDMA, rilapitypes/RIL_DEVICEINFO_SERIALNUMBER_GW
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: Rilapitypes.h, Ntddrilapitypes.h
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	rilapitypes.h
api_name:
-	RILDEVICEINFORMATION
product: Windows
targetos: Windows
req.typenames: RILDEVICEINFORMATION
---

# RILDEVICEINFORMATION Enumeration
<div class="alert"><b>Warning</b>  The Cellular COM API is deprecated in Windows 10. This content is provided to support maintenance of OEM and mobile operator created Windows Phone 8.1 applications.</div><div> </div>This enumeration describes the RILDEVICEINFORMATION.

## Syntax
````
enum RILDEVICEINFORMATION {
  RIL_DEVICEINFO_MANUFACTURER       = 0x01, 
  RIL_DEVICEINFO_MODEL              = 0x02, 
  RIL_DEVICEINFO_REVISION           = 0x03, 
  RIL_DEVICEINFO_SERIALNUMBER_GW    = 0x04, 
  RIL_DEVICEINFO_SERIALNUMBER_CDMA  = 0x05, 
  RIL_DEVICEINFO_ARG_SMALLEST       = RIL_DEVICEINFO_MANUFACTURER, 
  RIL_DEVICEINFO_ARG_LARGEST        = RIL_DEVICEINFO_SERIALNUMBER_CDMA 

};
````

## Constants

<table>
            
                <tr>
                    <td>RIL_DEVICEINFO_ARG_LARGEST</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DEVICEINFO_ARG_SMALLEST</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DEVICEINFO_MANUFACTURER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DEVICEINFO_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DEVICEINFO_MIN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DEVICEINFO_MODEL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DEVICEINFO_REVISION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DEVICEINFO_SERIALNUMBER_CDMA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_DEVICEINFO_SERIALNUMBER_GW</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h (include Rilapitypes.h, Ntddrilapitypes.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn946509">Cellular COM enumerations</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20RILDEVICEINFORMATION enumeration%20 RELEASE:%20(2/16/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>