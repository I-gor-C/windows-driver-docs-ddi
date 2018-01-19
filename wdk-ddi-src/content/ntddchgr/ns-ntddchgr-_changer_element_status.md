---
UID : NS:ntddchgr._CHANGER_ELEMENT_STATUS
title : _CHANGER_ELEMENT_STATUS
author : windows-driver-content
description : The ChangerGetElementStatus routine returns status information in this structure.
old-location : storage\changer_element_status.htm
old-project : storage
ms.assetid : 3debcf76-bb84-48ec-933e-03e099ad764f
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _CHANGER_ELEMENT_STATUS, *PCHANGER_ELEMENT_STATUS, CHANGER_ELEMENT_STATUS
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
req.alt-api : CHANGER_ELEMENT_STATUS
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
req.typenames : "*PCHANGER_ELEMENT_STATUS, CHANGER_ELEMENT_STATUS"
---

# _CHANGER_ELEMENT_STATUS structure
The <a href="..\mcd\nf-mcd-changergetelementstatus.md">ChangerGetElementStatus</a> routine returns status information in this structure.

## Syntax
````
typedef struct _CHANGER_ELEMENT_STATUS {
  CHANGER_ELEMENT Element;
  CHANGER_ELEMENT SrcElementAddress;
  ULONG           Flags;
  ULONG           ExceptionCode;
  UCHAR           TargetId;
  UCHAR           Lun;
  USHORT          Reserved;
  UCHAR           PrimaryVolumeID[MAX_VOLUME_ID_SIZE];
  UCHAR           AlternateVolumeID[MAX_VOLUME_ID_SIZE];
} CHANGER_ELEMENT_STATUS, *PCHANGER_ELEMENT_STATUS;
````

## Members

        
            `AlternateVolumeID`

            Specifies alternate volume identification for the media. This member is valid for two-sided media only, and pertains to the ID of the inverted side. It never represents a bar code. The miniclass driver must set <b>AlternateVolumeID</b> to the value previously assigned to the media using the <b>ChangerQueryVolumeTags</b> routine with an ASSERT_ALTERNATE or REPLACE_ALTERNATE action. The identifier must be no larger than MAX_VOLUME_ID_SIZE bytes and is valid only if ELEMENT_STATUS_AVOLTAG is also set in <b>Flags</b>.
        
            `Element`

            Specifies the element of type <a href="..\ntddchgr\ns-ntddchgr-_changer_element.md">CHANGER_ELEMENT</a>  to which this structure refers.
        
            `ExceptionCode`

            Indicates that the element is in an abnormal state. This member is valid only if ELEMENT_STATUS_EXCEPT is set in <b>Flags</b>. <b>ExceptionCode</b> can be set to one of the following values.
        
            `Flags`

            Indicates the status of the element, which can be one or more of the following values.
        
            `Lun`

            Specifies the SCSI device number of the drive at this element address. This member is valid only if <b>ElementType</b> in the <b>Element</b> member is <b>ChangerDrive</b> and ELEMENT_STATUS_LUN_VALID is set in <b>Flags</b>.
        
            `PrimaryVolumeID`

            Specifies the primary volume identifier for the media. If the changer supports a bar code reader and the reader is installed (as indicated by CHANGER_BAR_CODE_SCANNER_INSTALLED in <b>Features0</b> of GET_CHANGER_PARAMETERS), the miniclass driver must set <b>PrimaryVolumeID</b> to the bar code of the media. If the changer does not support a bar code reader, the miniclass driver should set <b>PrimaryVolumeID</b> to the value previously assigned to the media using the <b>ChangerQueryVolumeTags</b> routine with an ASSERT_PRIMARY or REPLACE_PRIMARY action. This member is valid only if ELEMENT_STATUS_PVOLTAG is also set in <b>Flags</b>. If the volume identifier is missing or unreadable, the miniclass driver should clear this flag and set the appropriate error status. This identifier must be no larger than MAX_VOLUME_ID_SIZE bytes.
        
            `Reserved`

            Reserved for future use. The value of this member must be zero.
        
            `SrcElementAddress`

            Specifies the element of type <a href="..\ntddchgr\ns-ntddchgr-_changer_element.md">CHANGER_ELEMENT</a> from which the media currently in this element was most recently moved. This member is valid only if ELEMENT_STATUS_SVALID is also set in <b>Flags</b>. This value must be a zero-based offset from the device-unique value.
        
            `TargetId`

            Specifies the SCSI target ID of the drive at this element address for a SCSI changer. This member is valid only if <b>ElementType</b> in the <b>Element</b> member is <b>ChangerDrive</b> and ELEMENT_STATUS_ID_VALID is set in <b>Flags</b>.

    ## Remarks
        For most element types, changer miniclass drivers use CHANGER_ELEMENT_STATUS to report the status of specified elements to the changer class driver. Some elements of type <b>ChangerDrive</b>, however, return product information data. If the device provides product information, the miniclass driver will report the element status data in a structure of type <a href="..\ntddchgr\ns-ntddchgr-_changer_element_status_ex.md">CHANGER_ELEMENT_STATUS_EX</a> instead of using CHANGER_ELEMENT_STATUS. The miniclass driver indicates that product information is present by setting ELEMENT_STATUS_PRODUCT_DATA in the <b>Flags</b> member of the structure.

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
<a href="..\ntddchgr\ns-ntddchgr-_changer_element.md">CHANGER_ELEMENT</a>
</dt>
<dt>
<a href="..\mcd\nf-mcd-changergetelementstatus.md">ChangerGetElementStatus</a>
</dt>
<dt>
<a href="..\mcd\nf-mcd-changerqueryvolumetags.md">ChangerQueryVolumeTags</a>
</dt>
<dt>
<a href="..\ntddchgr\ns-ntddchgr-_changer_element_status_ex.md">CHANGER_ELEMENT_STATUS_EX</a>
</dt>
<dt>
<a href="..\ntddchgr\ni-ntddchgr-ioctl_changer_get_element_status.md">IOCTL_CHANGER_GET_ELEMENT_STATUS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20CHANGER_ELEMENT_STATUS structure%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>