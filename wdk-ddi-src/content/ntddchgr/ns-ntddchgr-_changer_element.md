---
UID : NS:ntddchgr._CHANGER_ELEMENT
title : _CHANGER_ELEMENT
author : windows-driver-content
description : The CHANGER_ELEMENT structure contains a description of a changer element.
old-location : storage\changer_element.htm
old-project : storage
ms.assetid : 85035147-0ae8-482a-9a12-1e4e53ae1969
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _CHANGER_ELEMENT, CHANGER_ELEMENT, *PCHANGER_ELEMENT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddchgr.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : CHANGER_ELEMENT
req.alt-loc : ntddchgr.h
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
req.typenames : CHANGER_ELEMENT, *PCHANGER_ELEMENT
---

# _CHANGER_ELEMENT structure
The CHANGER_ELEMENT structure contains a description of a changer element.

## Syntax
````
typedef struct _CHANGER_ELEMENT {
  ELEMENT_TYPE ElementType;
  ULONG        ElementAddress;
} CHANGER_ELEMENT, *PCHANGER_ELEMENT;
````

## Members

        
            `ElementAddress`

            Indicates the element's zero-based address used by the system. A changer miniclass driver is responsible for translating this address to the device-specific address used by the changer.
        
            `ElementType`

            Indicates the type of element. Can be one of the following values taken from the <a href="..\ntddchgr\ne-ntddchgr-_element_type.md">ELEMENT_TYPE</a> enumeration.

    ## Remarks
        CHANGER_ELEMENT is used by both the changer class driver and a changer miniclass driver to describe a changer element. 

On input, a changer miniclass driver must translate the zero-based address in <b>ElementAddress</b> to a device-specific address before accessing the element. On output, the driver must translate a device-specific address to the zero-based equivalent before filling in <b>ElementAddress</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddchgr.h |

    ## See Also

        <dl>
<dt>
<a href="..\ntddchgr\ns-ntddchgr-_changer_element_list.md">CHANGER_ELEMENT_LIST</a>
</dt>
<dt>
<a href="..\ntddchgr\ns-ntddchgr-_changer_element_status.md">CHANGER_ELEMENT_STATUS</a>
</dt>
<dt>
<a href="..\ntddchgr\ne-ntddchgr-_element_type.md">ELEMENT_TYPE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20CHANGER_ELEMENT structure%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>