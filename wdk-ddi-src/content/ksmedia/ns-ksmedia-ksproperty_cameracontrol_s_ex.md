---
UID : NS:ksmedia.KSPROPERTY_CAMERACONTROL_S_EX
title : KSPROPERTY_CAMERACONTROL_S_EX
author : windows-driver-content
description : Specifies a camera control operation, including setting the flash, the image pin control properties, the region of interest in the image, or video stabilization.
old-location : stream\ksproperty_cameracontrol_s_ex.htm
old-project : stream
ms.assetid : fa015adf-93b6-472f-8a78-a627a59c032e
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KSPROPERTY_CAMERACONTROL_S_EX, KSPROPERTY_CAMERACONTROL_S_EX, *PKSPROPERTY_CAMERACONTROL_S_EX
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
req.alt-api : KSPROPERTY_CAMERACONTROL_S_EX
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
req.typenames : KSPROPERTY_CAMERACONTROL_S_EX, *PKSPROPERTY_CAMERACONTROL_S_EX
---

# KSPROPERTY_CAMERACONTROL_S_EX structure
Specifies a camera control operation, including setting the flash, the image pin control properties, the region of interest in the image, or video stabilization. This structure describes filter-based properties in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567802">PROPSETID_VIDCAP_CAMERACONTROL</a> property set.

Supported starting with Windows 8.

## Syntax
````
typedef struct {
  KSPROPERTY Property;
  LONG       Value;
  ULONG      Flags;
  ULONG      Capabilities;
  RECT       FocusRect;
} KSPROPERTY_CAMERACONTROL_S_EX, *PKSPROPERTY_CAMERACONTROL_S_EX;
````

## Members

        
            `Capabilities`

            If set, indicates that when the application submits a query, the driver should return the value of the <b>Capabilities</b> member of the appropriate camera control structure from the following list.

<ul>
<li>
<a href="..\ksmedia\ns-ksmedia-ksproperty_cameracontrol_flash_s.md">KSPROPERTY_CAMERACONTROL_FLASH_S</a>
</li>
<li>
<a href="..\ksmedia\ns-ksmedia-ksproperty_cameracontrol_image_pin_capability_s.md">KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_S</a>
</li>
<li>
<a href="..\ksmedia\ns-ksmedia-ksproperty_cameracontrol_region_of_interest_s.md">KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S</a>
</li>
<li>
<a href="..\ksmedia\ns-ksmedia-ksproperty_cameracontrol_videostabilization_mode_s.md">KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S</a>
</li>
</ul>
        
            `Flags`

            Indicates, for Get requests, the current setting for the specified property from the values listed below. Indicates, for Set requests, the desired setting for the specified property from the values listed below. This member can be a bitwise <b>OR</b> of the following values that are defined in Ksmedia.h:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `FocusRect`

            A <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure that specifies the rectangular region in which the device should set the focus. This structure is available only to Windows desktop applications.
        
            `Property`

            Specifies an initialized <a href="..\ks\nf-ks-ikscontrol-ksproperty.md">KSPROPERTY</a> structure that describes the property set, property ID, and request type.
        
            `Value`

            Specifies the value of the property. This member is read/write.

    ## Remarks
        When a requested camera focus operation is completed or is canceled, the driver should generate an event specified by the <b>KSEVENT_CAMERACONTROL_FOCUS</b> enumeration value.

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
<a href="..\ksmedia\ne-ksmedia-ksevent_cameracontrol.md">KSEVENT_CAMERACONTROL</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ikscontrol-ksproperty.md">KSPROPERTY</a>
</dt>
<dt>
<a href="..\ksmedia\ns-ksmedia-ksproperty_cameracontrol_flash_s.md">KSPROPERTY_CAMERACONTROL_FLASH_S</a>
</dt>
<dt>
<a href="..\ksmedia\ns-ksmedia-ksproperty_cameracontrol_region_of_interest_s.md">KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S</a>
</dt>
<dt>
<a href="..\ksmedia\ns-ksmedia-ksproperty_cameracontrol_videostabilization_mode_s.md">KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_CAMERACONTROL_S_EX structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>