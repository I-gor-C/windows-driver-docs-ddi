---
UID: NS.ntddchgr._CHANGER_ELEMENT_STATUS_EX
title: CHANGER_ELEMENT_STATUS_EX
author: windows-driver-content
description: The ChangerGetElementStatus routine returns status information in this structure.
old-location: storage\changer_element_status_ex.htm
old-project: storage
ms.assetid: 1fb0d0f9-711a-4bd4-baf6-38ccbeae6e4a
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: CHANGER_ELEMENT_STATUS_EX, CHANGER_ELEMENT_STATUS_EX, *PCHANGER_ELEMENT_STATUS_EX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddchgr.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CHANGER_ELEMENT_STATUS_EX
req.alt-loc: ntddchgr.h
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
req.iface: 
---

# CHANGER_ELEMENT_STATUS_EX structure



## -description
<p>The <a href="..\mcd\nf-mcd-changergetelementstatus.md">ChangerGetElementStatus</a> routine returns status information in this structure. </p>


## -syntax

````
typedef struct _CHANGER_ELEMENT_STATUS_EX {
  CHANGER_ELEMENT Element;
  CHANGER_ELEMENT SrcElementAddress;
  ULONG           Flags;
  ULONG           ExceptionCode;
  UCHAR           TargetId;
  UCHAR           Lun;
  USHORT          Reserved;
  UCHAR           PrimaryVolumeID[MAX_VOLUME_ID_SIZE];
  UCHAR           AlternateVolumeID[MAX_VOLUME_ID_SIZE];
  UCHAR           VendorIdentification[VENDOR_ID_LENGTH];
  UCHAR           ProductIdentification[PRODUCT_ID_LENGTH];
  UCHAR           SerialNumber[SERIAL_NUMBER_LENGTH];
} CHANGER_ELEMENT_STATUS_EX, *PCHANGER_ELEMENT_STATUS_EX;
````


## -struct-fields
<dl>

### -field <b>Element</b>

<dd>
<p>Specifies the element of type <a href="..\ntddchgr\ns-ntddchgr--changer-element.md">CHANGER_ELEMENT</a>  to which this structure refers.</p>
</dd>

### -field <b>SrcElementAddress</b>

<dd>
<p>Specifies the element of type <a href="..\ntddchgr\ns-ntddchgr--changer-element.md">CHANGER_ELEMENT</a> from which the media currently in this element was most recently moved. This member is valid only if ELEMENT_STATUS_SVALID is also set in <b>Flags</b>. This value must be a zero-based offset from the device-unique value.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Indicates the status of the element, which can be one or more of the following values.</p>
<dl class="indent">

### -field <a id="ELEMENT_STATUS_FULL"></a><a id="element_status_full"></a><p><a id="ELEMENT_STATUS_FULL"></a><a id="element_status_full"></a><b>ELEMENT_STATUS_FULL</b></p>


<dd>
<p>The element contains a piece of media. This flag is valid if <b>ElementType</b> in the <b>Element</b> member is <b>ChangerDrive</b>, <b>ChangerSlot</b>, or <b>ChangerTransport</b>. If <b>ElementType</b> is <b>ChangerIEPort</b>, this flag is valid only if CHANGER_REPORT_IEPORT_STATE is also set in <b>Features0</b> of <a href="..\ntddchgr\ns-ntddchgr--get-changer-parameters.md">GET_CHANGER_PARAMETERS</a>.</p>
</dd>

### -field <a id="ELEMENT_STATUS_IMPEXP"></a><a id="element_status_impexp"></a><p><a id="ELEMENT_STATUS_IMPEXP"></a><a id="element_status_impexp"></a><b>ELEMENT_STATUS_IMPEXP</b></p>


<dd>
<p>The media in this element was placed there by an operator. This flag is valid only if <b>ElementType</b> in the <b>Element</b> member is <b>ChangerIEPort</b>. </p>
</dd>

### -field <a id="ELEMENT_STATUS_EXCEPT"></a><a id="element_status_except"></a><p><a id="ELEMENT_STATUS_EXCEPT"></a><a id="element_status_except"></a><b>ELEMENT_STATUS_EXCEPT</b></p>


<dd>
<p>The element is in an abnormal state. Check the <b>ExceptionCode</b> member for more information.</p>
</dd>

### -field <a id="ELEMENT_STATUS_ACCESS"></a><a id="element_status_access"></a><p><a id="ELEMENT_STATUS_ACCESS"></a><a id="element_status_access"></a><b>ELEMENT_STATUS_ACCESS</b></p>


<dd>
<p>The changer's transport element can access the piece of media in this element. The miniclass driver clears this flag to indicate that the media is not accessible for one of the following reasons: If <b>ElementType</b> in the <b>Element</b> member is <b>ChangerSlot</b>, the slot is not present in the changer (for example, the magazine containing the slot has been physically removed). If <b>ElementType</b> is <b>ChangerDrive</b>, the drive is broken or has been removed. If <b>ElementType</b> is <b>ChangerIEPort</b>, the IEport is extended.</p>
</dd>

### -field <a id="ELEMENT_STATUS_EXENAB"></a><a id="element_status_exenab"></a><p><a id="ELEMENT_STATUS_EXENAB"></a><a id="element_status_exenab"></a><b>ELEMENT_STATUS_EXENAB</b></p>


<dd>
<p>The element supports export of media through the changer's IEport.</p>
</dd>

### -field <a id="ELEMENT_STATUS_INENAB"></a><a id="element_status_inenab"></a><p><a id="ELEMENT_STATUS_INENAB"></a><a id="element_status_inenab"></a><b>ELEMENT_STATUS_INENAB</b></p>


<dd>
<p>The element supports import of media through the changer's IEport.</p>
</dd>

### -field <a id="ELEMENT_STATUS_LUN_VALID"></a><a id="element_status_lun_valid"></a><p><a id="ELEMENT_STATUS_LUN_VALID"></a><a id="element_status_lun_valid"></a><b>ELEMENT_STATUS_LUN_VALID</b></p>


<dd>
<p>The device number in the <b>Lun</b> member is valid. This flag is valid only if <b>ElementType</b> in the <b>Element</b> member is <b>ChangerDrive</b>. </p>
</dd>

### -field <a id="ELEMENT_STATUS_ID_VALID"></a><a id="element_status_id_valid"></a><p><a id="ELEMENT_STATUS_ID_VALID"></a><a id="element_status_id_valid"></a><b>ELEMENT_STATUS_ID_VALID</b></p>


<dd>
<p>The SCSI target ID in the <b>TargetID</b> member is valid. This flag is valid only if <b>ElementType</b> in the <b>Element</b> member is <b>ChangerDrive</b>. </p>
</dd>

### -field <a id="ELEMENT_STATUS_NOT_BUS"></a><a id="element_status_not_bus"></a><p><a id="ELEMENT_STATUS_NOT_BUS"></a><a id="element_status_not_bus"></a><b>ELEMENT_STATUS_NOT_BUS</b></p>


<dd>
<p>The drive at the address indicated by <b>Lun</b> and <b>TargetID</b> is on a different SCSI bus than the changer itself. </p>
</dd>

### -field <a id="ELEMENT_STATUS_PRODUCT_DATA"></a><a id="element_status_product_data"></a><p><a id="ELEMENT_STATUS_PRODUCT_DATA"></a><a id="element_status_product_data"></a><b>ELEMENT_STATUS_PRODUCT_DATA</b></p>


<dd>
<p>The serial number in the <b>SerialNumber</b> member is valid.</p>
</dd>

### -field <a id="ELEMENT_STATUS_INVERT"></a><a id="element_status_invert"></a><p><a id="ELEMENT_STATUS_INVERT"></a><a id="element_status_invert"></a><b>ELEMENT_STATUS_INVERT</b></p>


<dd>
<p>The media in the element was flipped. This flag is valid only if the ELEMENT_STATUS_SVALID flag is also set.</p>
</dd>

### -field <a id="ELEMENT_STATUS_SVALID"></a><a id="element_status_svalid"></a><p><a id="ELEMENT_STATUS_SVALID"></a><a id="element_status_svalid"></a><b>ELEMENT_STATUS_SVALID</b></p>


<dd>
<p>The <b>SourceElement</b> member and ELEMENT_STATUS_INVERT flag are both valid.</p>
</dd>

### -field <a id="ELEMENT_STATUS_PVOLTAG"></a><a id="element_status_pvoltag"></a><p><a id="ELEMENT_STATUS_PVOLTAG"></a><a id="element_status_pvoltag"></a><b>ELEMENT_STATUS_PVOLTAG</b></p>


<dd>
<p>Primary volume information in the <b>PrimaryVolumeID</b> member is valid.</p>
</dd>

### -field <a id="ELEMENT_STATUS_AVOLTAG"></a><a id="element_status_avoltag"></a><p><a id="ELEMENT_STATUS_AVOLTAG"></a><a id="element_status_avoltag"></a><b>ELEMENT_STATUS_AVOLTAG</b></p>


<dd>
<p>Alternate volume information in the <b>AlternateVolumeID</b> member is valid.</p>
</dd>
</dl>
</dd>

### -field <b>ExceptionCode</b>

<dd>
<p>Indicates that the element is in an abnormal state. This member is valid only if ELEMENT_STATUS_EXCEPT is set in <b>Flags</b>. <b>ExceptionCode</b> can be set to one of the following values. </p>
<dl class="indent">

### -field <a id="ERROR_LABEL_UNREADABLE"></a><a id="error_label_unreadable"></a><p><a id="ERROR_LABEL_UNREADABLE"></a><a id="error_label_unreadable"></a><b>ERROR_LABEL_UNREADABLE</b></p>


<dd>
<p>The changer's bar code reader could not read the bar code label on the piece of media in this element, because the media is missing, damaged, improperly positioned, or upside down.</p>
</dd>

### -field <a id="ERROR_LABEL_QUESTIONABLE"></a><a id="error_label_questionable"></a><p><a id="ERROR_LABEL_QUESTIONABLE"></a><a id="error_label_questionable"></a><b>ERROR_LABEL_QUESTIONABLE</b></p>


<dd>
<p>The label might be invalid due to a unit attention condition.</p>
</dd>

### -field <a id="ERROR_SLOT_NOT_PRESENT"></a><a id="error_slot_not_present"></a><p><a id="ERROR_SLOT_NOT_PRESENT"></a><a id="error_slot_not_present"></a><b>ERROR_SLOT_NOT_PRESENT</b></p>


<dd>
<p>The slot at this element address is currently not installed in the changer. A miniclass driver sets this code for each slot in a removable magazine to indicate that the magazine has been removed.</p>
</dd>

### -field <a id="ERROR_DRIVE_NOT_INSTALLED"></a><a id="error_drive_not_installed"></a><p><a id="ERROR_DRIVE_NOT_INSTALLED"></a><a id="error_drive_not_installed"></a><b>ERROR_DRIVE_NOT_INSTALLED</b></p>


<dd>
<p>The drive at this element address is absent. If a changer can continue to operate without the drive, its miniclass driver sets ERROR_DRIVE_NOT_INSTALLED for the drive. </p>
</dd>

### -field <a id="ERROR_TRAY_MALFUNCTION"></a><a id="error_tray_malfunction"></a><p><a id="ERROR_TRAY_MALFUNCTION"></a><a id="error_tray_malfunction"></a><b>ERROR_TRAY_MALFUNCTION</b></p>


<dd>
<p>The drive at this element address has a tray that must be extended to load or remove media, and the tray is not extending as required.</p>
</dd>

### -field <a id="ERROR_UNHANDLED_ERROR"></a><a id="error_unhandled_error"></a><p><a id="ERROR_UNHANDLED_ERROR"></a><a id="error_unhandled_error"></a><b>ERROR_UNHANDLED_ERROR</b></p>


<dd>
<p>Unknown error condition.</p>
</dd>
</dl>
</dd>

### -field <b>TargetId</b>

<dd>
<p>Specifies the SCSI target ID of the drive at this element address for a SCSI changer. This member is valid only if <b>ElementType</b> in the <b>Element</b> member is <b>ChangerDrive</b> and ELEMENT_STATUS_ID_VALID is set in <b>Flags</b>. </p>
</dd>

### -field <b>Lun</b>

<dd>
<p>Specifies the SCSI device number of the drive at this element address. This member is valid only if <b>ElementType</b> in the <b>Element</b> member is <b>ChangerDrive</b> and ELEMENT_STATUS_LUN_VALID is set in <b>Flags</b>.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use. The value of this member must be zero.</p>
</dd>

### -field <b>PrimaryVolumeID</b>

<dd>
<p>Specifies the primary volume identifier for the media. If the changer supports a bar code reader and the reader is installed (as indicated by CHANGER_BAR_CODE_SCANNER_INSTALLED in <b>Features0</b> of <a href="..\ntddchgr\ns-ntddchgr--get-changer-parameters.md">GET_CHANGER_PARAMETERS</a>), the miniclass driver must set <b>PrimaryVolumeID</b> to the bar code of the media. If the changer does not support a bar code reader, the miniclass driver should set <b>PrimaryVolumeID</b> to the value previously assigned to the media using the <a href="..\mcd\nf-mcd-changerqueryvolumetags.md">ChangerQueryVolumeTags</a> routine with an ASSERT_PRIMARY or REPLACE_PRIMARY action. This member is valid only if ELEMENT_STATUS_PVOLTAG is also set in <b>Flags</b>. If the volume identifier is missing or unreadable, the miniclass driver should clear this flag and set the appropriate error status. This identifier must be no larger than MAX_VOLUME_ID_SIZE bytes. </p>
</dd>

### -field <b>AlternateVolumeID</b>

<dd>
<p>Specifies alternate volume identification for the media. This member is valid for two-sided media only, and pertains to the ID of the inverted side. It never represents a bar code. The miniclass driver must set <b>AlternateVolumeID</b> to the value previously assigned to the media using the <a href="..\mcd\nf-mcd-changerqueryvolumetags.md">ChangerQueryVolumeTags</a> routine with an ASSERT_ALTERNATE or REPLACE_ALTERNATE action. The identifier must be no larger than MAX_VOLUME_ID_SIZE bytes and is valid only if ELEMENT_STATUS_AVOLTAG is also set in <b>Flags</b>.</p>
</dd>

### -field <b>VendorIdentification</b>

<dd>
<p>Contains the vendor ID. This identifier must be no larger than VENDOR_ID_LENGTH bytes. </p>
</dd>

### -field <b>ProductIdentification</b>

<dd>
<p>Contains the product ID. This identifier must be no larger than PRODUCT_ID_LENGTH bytes. </p>
</dd>

### -field <b>SerialNumber</b>

<dd>
<p>Contains the serial number. This identifier must be no larger than SERIAL_NUMBER_LENGTH bytes. </p>
</dd>
</dl>

## -remarks
<p>The <a href="..\mcd\nf-mcd-changergetelementstatus.md">ChangerGetElementStatus</a> routine returns status information in this structure if vendor, product, or serial number information is needed. Otherwise, <b>ChangerGetElementStatus</b> returns status information in the <a href="..\ntddchgr\ns-ntddchgr--changer-element-status.md">CHANGER_ELEMENT_STATUS</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddchgr.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddchgr\ns-ntddchgr--changer-element-status.md">CHANGER_ELEMENT_STATUS</a>
</dt>
<dt>
<a href="..\mcd\nf-mcd-changergetelementstatus.md">ChangerGetElementStatus</a>
</dt>
<dt>
<a href="..\ntddchgr\ns-ntddchgr--changer-element.md">CHANGER_ELEMENT</a>
</dt>
<dt>
<a href="..\ntddchgr\ns-ntddchgr--get-changer-parameters.md">GET_CHANGER_PARAMETERS</a>
</dt>
<dt>
<a href="..\ntddchgr\ni-ntddchgr-ioctl-changer-get-element-status.md">IOCTL_CHANGER_GET_ELEMENT_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20CHANGER_ELEMENT_STATUS_EX structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
