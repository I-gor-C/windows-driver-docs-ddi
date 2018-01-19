---
UID : NS:ks.KSP_PIN
title : KSP_PIN
author : windows-driver-content
description : Kernel streaming clients use the KSP_PIN structure to specify the property and pin type within a KSPROPSETID_Pin property request.
old-location : stream\ksp_pin.htm
old-project : stream
ms.assetid : 0be4c4e1-6ea6-4439-841d-088cb1902604
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KSP_PIN, *PKSP_PIN, KSP_PIN
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ks.h
req.include-header : Ks.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KSP_PIN
req.alt-loc : ks.h
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
req.typenames : "*PKSP_PIN, KSP_PIN"
---

# KSP_PIN structure
Kernel streaming clients use the KSP_PIN structure to specify the property and pin type within a KSPROPSETID_Pin property request.

## Syntax
````
typedef struct {
  KSPROPERTY Property;
  ULONG      PinId;
  union {
    ULONG Reserved;
    ULONG Flags;
  };
  ULONG      Reserved;
} KSP_PIN, *PKSP_PIN;
````

## Members

        
            `PinId`

            Specifies the pin type ID.
        
            `Property`

            Specifies a <a href="..\ks\nf-ks-ikscontrol-ksproperty.md">KSPROPERTY</a> structure.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ks\nf-ks-ikscontrol-ksproperty.md">KSPROPERTY</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSP_PIN structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>