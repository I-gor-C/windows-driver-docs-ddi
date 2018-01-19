---
UID : NS:ksmedia.KSPROPERTY_CAMERACONTROL_FLASH_S
title : KSPROPERTY_CAMERACONTROL_FLASH_S
author : windows-driver-content
description : Describes flash control properties in the PROPSETID_VIDCAP_CAMERACONTROL_FLASH camera control property set. This structure specifies property values that are used by applications to configure the camera's flash.
old-location : stream\ksproperty_cameracontrol_flash_s.htm
old-project : stream
ms.assetid : 5d02c019-9a4a-458a-8361-7597bb1fe1a2
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KSPROPERTY_CAMERACONTROL_FLASH_S, *PKSPROPERTY_CAMERACONTROL_FLASH_S, KSPROPERTY_CAMERACONTROL_FLASH_S
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ksmedia.h
req.include-header : Ksmedia.h
req.target-type : Windows
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KSPROPERTY_CAMERACONTROL_FLASH_S
req.alt-loc : Ksmedia.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PKSPROPERTY_CAMERACONTROL_FLASH_S, KSPROPERTY_CAMERACONTROL_FLASH_S"
---

# KSPROPERTY_CAMERACONTROL_FLASH_S structure
Describes flash control properties in the <b>PROPSETID_VIDCAP_CAMERACONTROL_FLASH</b> camera control property set. This structure specifies property values that are used by applications to configure the camera's flash.

## Syntax
````
typedef struct {
  ULONG Flash;
  ULONG Capabilities;
} KSPROPERTY_CAMERACONTROL_FLASH_S, *PKSPROPERTY_CAMERACONTROL_FLASH_S;
````

## Members

        
            `Capabilities`

            Indicates the flash modes that the device supports. This value is a bitwise <b>OR</b> of these possible values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `Flash`

            Indicates requested flash settings. This value must be one of these possible values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ksmedia.h (include Ksmedia.h) |

    ## See Also

        <dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj156041">KSPROPERTY_CAMERACONTROL_FLASH_PROPERTY</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_CAMERACONTROL_FLASH_S structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>