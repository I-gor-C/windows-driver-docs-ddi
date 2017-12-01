---
UID: NS.ntddchgr._GET_CHANGER_PARAMETERS
title: GET_CHANGER_PARAMETERS
author: windows-driver-content
description: Retrieves the characteristics of the changer.
old-location: storage\get_changer_parameters.htm
old-project: storage
ms.assetid: c9a47406-5dd2-4cda-b241-3a439406ac75
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: GET_CHANGER_PARAMETERS, GET_CHANGER_PARAMETERS, *PGET_CHANGER_PARAMETERS
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
req.alt-api: GET_CHANGER_PARAMETERS
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

# GET_CHANGER_PARAMETERS structure



## -description
<p>Retrieves the characteristics of the changer. </p>


## -syntax

````
typedef struct _GET_CHANGER_PARAMETERS {
  ULONG  Size;
  USHORT NumberTransportElements;
  USHORT NumberStorageElements;
  USHORT NumberCleanerSlots;
  USHORT NumberIEElements;
  USHORT NumberDataTransferElements;
  USHORT NumberOfDoors;
  USHORT FirstSlotNumber;
  USHORT FirstDriveNumber;
  USHORT FirstTransportNumber;
  USHORT FirstIEPortNumber;
  USHORT FirstCleanerSlotAddress;
  USHORT MagazineSize;
  ULONG  DriveCleanTimeout;
  ULONG  Features0;
  ULONG  Features1;
  UCHAR  MoveFromTransport;
  UCHAR  MoveFromSlot;
  UCHAR  MoveFromIePort;
  UCHAR  MoveFromDrive;
  UCHAR  ExchangeFromTransport;
  UCHAR  ExchangeFromSlot;
  UCHAR  ExchangeFromIePort;
  UCHAR  ExchangeFromDrive;
  UCHAR  LockUnlockCapabilities;
  UCHAR  PositionCapabilities;
  UCHAR  Reserved1[2];
  ULONG  Reserved2[2];
} GET_CHANGER_PARAMETERS, *PGET_CHANGER_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of this structure in bytes. Set to <b>sizeof</b>(GET_CHANGER_PARAMETERS). In effect, this member indicates the version of this structure being used by the miniclass driver. </p>
</dd>

### -field <b>NumberTransportElements</b>

<dd>
<p>Indicates the number of transport elements in the changer. For a SCSI changer, this is defined in the element address page. This value is almost always 1, because most changers have a single transport element, which can have one or two picker mechanisms. A changer that has two picker mechanisms on its transport must not be represented as having two transports, because pickers cannot be addressed individually. High-end media libraries can have dual and multiple transport elements for fault tolerance.</p>
</dd>

### -field <b>NumberStorageElements</b>

<dd>
<p>Indicates the number of storage elements (slots) in the changer. For a SCSI changer, this is defined in the element address page. This value represents the maximum number of slots available for this changer, including those in removable magazines, whether the magazines are installed. If <b>NumberCleanerSlots</b> is 1, then <b>NumberStorageElements</b> is 1 less than the maximum number of slots in the changer.</p>
</dd>

### -field <b>NumberCleanerSlots</b>

<dd>
<p>Indicates the number of storage elements (slots) for cleaner cartridges in the changer. For a SCSI changer, this value is not reported in mode sense data, so the miniclass driver must provide it. The miniclass driver should set <b>NumberCleanerSlots</b> to 1 only if the operator's guide for the changer identifies a specific slot as a cleaner slot. If <b>NumberCleanerSlots</b> is 1, then <b>FirstCleanerSlotAddress</b> indicates the zero-based address of the slot in which a drive cleaner should be inserted. If the changer does not support drive cleaning by programmatically moving the cleaner cartridge from its slot to a drive, the miniclass driver must set <b>NumberCleanerSlots</b> to 0. <b>NumberCleanerSlots</b> must not be greater than 1.</p>
</dd>

### -field <b>NumberIEElements</b>

<dd>
<p>Indicates the number of IEport elements the changer has for inserting and ejecting of media. For a SCSI changer, this is defined in the element address page. An IEport element must not be part of the storage element (slot) space, and it must be possible to transport media between the IEport and a slot using a MOVE MEDIUM SCSI command. If the changer has a door and not a true IEport, the miniclass driver must set <b>NumberIEElements</b> to 0.</p>
</dd>

### -field <b>NumberDataTransferElements</b>

<dd>
<p>Indicates the number of data transfer elements (drives) in the changer. For a SCSI changer, this is defined in the element address page. Unlike <b>NumberStorageElements</b>, which indicates the total number of possible slots whether the slots are actually present, <b>NumberDataTransferElements</b> indicates the number of drives that are actually present in the changer.</p>
</dd>

### -field <b>NumberOfDoors</b>

<dd>
<p>Indicates the number of doors that the changer has. For a SCSI changer, this value is not reported in mode sense data, so the miniclass driver must provide it. A door provides access to all media in the changer at once, unlike an IEport which provides access to one or more, but not all, media. A changer's door can be a physical front door or a single magazine that contains all media. If a changer supports only an IEport for inserting and ejecting media, the <b>NumberOfDoors</b> must be 0.</p>
</dd>

### -field <b>FirstSlotNumber</b>

<dd>
<p>Indicates the number used by the changer vendor to identify the first storage element (slot) in the changer to the end user, either by marking a magazine or by defining a slot numbering scheme in the changer's operators guide. <b>FirstSlotNumber</b> is typically 0 or 1, but it can be the first address in a consecutive range of slot addresses defined by the vendor. </p>
</dd>

### -field <b>FirstDriveNumber</b>

<dd>
<p>Indicates the number used by the changer vendor to identify the first data transfer element (drive) in the changer to the end user. <b>FirstDriveNumber</b> is typically 0 or 1, but it can be the first address in a consecutive range of drive addresses defined by the vendor. </p>
</dd>

### -field <b>FirstTransportNumber</b>

<dd>
<p>Indicates the number used by the changer vendor to identify the first (and usually only) transport element in the changer to the end user. <b>FirstTransportNumber</b> is typically 0 or 1, but it can be the first address in a consecutive range of transport addresses defined by the vendor. </p>
</dd>

### -field <b>FirstIEPortNumber</b>

<dd>
<p>Indicates the number used by the changer vendor to identify the first (and usually only) IEport in the changer to the end user. <b>FirstIEPortNumber</b> is typically 0 or 1, but it can be the first address in a consecutive range of IEport addresses defined by the vendor. If <b>NumberIEElements</b> is 0, <b>FirstIEPortNumber</b> must also be 0.</p>
</dd>

### -field <b>FirstCleanerSlotAddress</b>

<dd>
<p>Indicates the number used by the changer vendor to identify the first (and only) slot address assigned to a drive cleaner cartridge to the end user. This must be the value defined by the vendor in the changer's operators guide. For example, if a changer has 8 slots numbered 1 through 8 and its operator's guide designates slot 8 as the drive cleaner slot, <b>FirstSlotNumber</b> would be 1 and <b>FirstCleanerSlotAddress</b> would be 8. If the same 8 slots were numbered 0 through 7, <b>FirstSlotNumber</b> would be 0 and <b>FirstCleanerSlotAddress</b> would be 7. If <b>NumberCleanerSlots</b> is 0, <b>FirstCleanerSlotAddress</b> must be 0.</p>
</dd>

### -field <b>MagazineSize</b>

<dd>
<p>Indicates the number of slots in the removable magazines in the changer. This member is valid only if CHANGER_CARTRIDGE_MAGAZINE is set in <b>Features0</b>.</p>
</dd>

### -field <b>DriveCleanTimeout</b>

<dd>
<p>Indicates twice the maximum number of seconds a cleaning is expected to take. The changer's drives should be cleaned by its cleaner cartridge in half the time specified by <b>DriveCleanTimeout</b>. For example, if a drive is typically cleaned in 300 seconds (5 minutes), <b>DriveCleanTimeout</b> should be set to 600.</p>
</dd>

### -field <b>Features0</b>

<dd>
<p>Indicates the features supported by the changer. This member can have one or more of the following values bitwise ORed together.</p>
<p></p>
<dl>

### -field <a id="CHANGER_BAR_CODE_SCANNER_INSTALLED"></a><a id="changer_bar_code_scanner_installed"></a>CHANGER_BAR_CODE_SCANNER_INSTALLED

<dd>
<p>The changer supports a bar code reader and the reader is installed. A miniclass driver must not hardcode this flag unless the changer's bar code reader is always installed. If the bar code reader is optional, the miniclass driver must determine whether the reader is actually installed and set the flag accordingly.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_INIT_ELEM_STAT_WITH_RANGE"></a><a id="changer_init_elem_stat_with_range"></a>CHANGER_INIT_ELEM_STAT_WITH_RANGE

<dd>
<p>The changer can initialize elements within a specified range. For a SCSI changer, this flag indicates whether the changer supports the INITIALIZE ELEMENT STATUS WITH RANGE SCSI command.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_CLOSE_IEPORT"></a><a id="changer_close_ieport"></a>CHANGER_CLOSE_IEPORT

<dd>
<p>The changer has an IEport and can retract the IEport programmatically.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_OPEN_IEPORT"></a><a id="changer_open_ieport"></a>CHANGER_OPEN_IEPORT

<dd>
<p>The changer has an IEport and can extend the IEport programmatically. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_STATUS_NON_VOLATILE"></a><a id="changer_status_non_volatile"></a>CHANGER_STATUS_NON_VOLATILE

<dd>
<p>The changer uses nonvolatile memory for element status information.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_EXCHANGE_MEDIA"></a><a id="changer_exchange_media"></a>CHANGER_EXCHANGE_MEDIA

<dd>
<p>Supports EXCHANGE MEDIUM SCSI command either by handling two volumes at a time or by using other changer elements to emulate this capability.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_CLEANER_SLOT"></a><a id="changer_cleaner_slot"></a>CHANGER_CLEANER_SLOT

<dd>
<p>Indicates that the changer has a specific slot designated for a cleaner cartridge. If this flag is set, <b>NumberCleanerSlots</b> must be one and <b>FirstCleanerSlotAddress</b> must specify the address of the cleaner slot. This bit can only be set if CHANGER_DRIVE_CLEANING_REQUIRED is set and CHANGER_CLEANER_OPS_NOT_SUPPORTED is reset. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_LOCK_UNLOCK"></a><a id="changer_lock_unlock"></a>CHANGER_LOCK_UNLOCK

<dd>
<p>The changer's door, IEport, or keypad can be locked or unlocked programmatically. If this flag is set, <b>LockUnlockCapabilities</b> indicates which elements can be locked or unlocked.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_CARTRIDGE_MAGAZINE"></a><a id="changer_cartridge_magazine"></a>CHANGER_CARTRIDGE_MAGAZINE

<dd>
<p>The changer uses removable cartridge magazines for some or all storage slots.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_MEDIUM_FLIP"></a><a id="changer_medium_flip"></a>CHANGER_MEDIUM_FLIP

<dd>
<p>The changer's transport element supports flipping (rotating) media. For a SCSI changer, this flag reflects the rotate bit in the transport geometry parameters page. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_POSITION_TO_ELEMENT"></a><a id="changer_position_to_element"></a>CHANGER_POSITION_TO_ELEMENT

<dd>
<p>The changer can position the transport to a particular destination. For a SCSI changer, this flag indicates whether the changer supports the POSITION TO ELEMENT SCSI command. If this flag is set, <b>PositionCapabilities</b> indicates the elements to which the transport can be positioned.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_REPORT_IEPORT_STATE"></a><a id="changer_report_ieport_state"></a>CHANGER_REPORT_IEPORT_STATE

<dd>
<p>The changer can report whether media is present in the IEport. Such a changer must have a sensor in the IEport to detect the presence or absence of media. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_STORAGE_DRIVE"></a><a id="changer_storage_drive"></a>CHANGER_STORAGE_DRIVE

<dd>
<p>The changer can use a drive as an independent storage element; that is, it can store media in the drive without reading it. For a SCSI changer, this flag reflects the state of the DT bit in the device capabilities page. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_STORAGE_IEPORT"></a><a id="changer_storage_ieport"></a>CHANGER_STORAGE_IEPORT

<dd>
<p>The changer can use an IEport as an independent storage element. For a SCSI changer, this flag reflects the state of the I/E bit in the device capabilities page. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_STORAGE_SLOT"></a><a id="changer_storage_slot"></a>CHANGER_STORAGE_SLOT

<dd>
<p>The changer can use a slot as an independent storage element for media. For a SCSI changer, this flag reflects the state of the ST bit in the device capabilities page. Slots are the normal storage location for media, so the changer must support this functionality.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_STORAGE_TRANSPORT"></a><a id="changer_storage_transport"></a>CHANGER_STORAGE_TRANSPORT

<dd>
<p>The changer can use a transport as an independent storage element. For a SCSI changer, this flag reflects the state of the MT bit in the device capabilities page. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_DRIVE_CLEANING_REQUIRED"></a><a id="changer_drive_cleaning_required"></a>CHANGER_DRIVE_CLEANING_REQUIRED

<dd>
<p>Indicates that the changer's drives might periodically report sense codes that indicate that the drive requires cleaning.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_PREDISMOUNT_EJECT_REQUIRED"></a><a id="changer_predismount_eject_required"></a>CHANGER_PREDISMOUNT_EJECT_REQUIRED

<dd>
<p>The changer requires an explicit command issued through a mass storage driver (tape, disk, or CD-ROM, for example) to eject media from a drive before the changer can move the media from a drive to a slot. If the changer ejects media automatically, the miniclass driver should clear this flag.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_CLEANER_ACCESS_NOT_VALID"></a><a id="changer_cleaner_access_not_valid"></a>CHANGER_CLEANER_ACCESS_NOT_VALID

<dd>
<p>The ELEMENT_STATUS_ACCESS flag in a CHANGER_ELEMENT_STATUS structure for a data transport element is invalid when the transport element contains a cleaning cartridge.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_DRIVE_EMPTY_ON_DOOR_ACCESS"></a><a id="changer_drive_empty_on_door_access"></a>CHANGER_DRIVE_EMPTY_ON_DOOR_ACCESS

<dd>
<p>The changer requires all drives to be empty (dismounted) before they can be accessed through its door. The miniclass driver should set this flag if the changer has static-sensitive drives that could be affected by an operator gaining access to the inside of the changer, or if the changer automatically ejects media from its drives when the operator attempts to physically open the door. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_VOLUME_IDENTIFICATION"></a><a id="changer_volume_identification"></a>CHANGER_VOLUME_IDENTIFICATION

<dd>
<p>The changer supports volume identification. For a SCSI changer, this flag indicates whether the changer supports the SEND VOLUME TAG and REQUEST VOLUME ELEMENT ADDRESS SCSI commands. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_VOLUME_SEARCH"></a><a id="changer_volume_search"></a>CHANGER_VOLUME_SEARCH

<dd>
<p>The changer can search for volume information. For a SCSI changer, this flag indicates whether the changer supports the supports the SEND VOLUME TAG SCSI SCSI command with a send action code of TRANSLATE. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_VOLUME_ASSERT"></a><a id="changer_volume_assert"></a>CHANGER_VOLUME_ASSERT

<dd>
<p>The changer can verify volume information. For a SCSI changer, this flag indicates whether the changer supports the SEND VOLUME TAG SCSI command with a send action code of ASSERT.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_VOLUME_REPLACE"></a><a id="changer_volume_replace"></a>CHANGER_VOLUME_REPLACE

<dd>
<p>The changer can replace volume information. For a SCSI changer, this flag indicates whether the changer supports the SEND VOLUME TAG SCSI command with a send action code of REPLACE. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_VOLUME_UNDEFINE"></a><a id="changer_volume_undefine"></a>CHANGER_VOLUME_UNDEFINE

<dd>
<p>The changer can clear existing volume information. For a SCSI changer, this flag indicates whether the changer supports the supports the SEND VOLUME TAG SCSI command with a send action code of UNDEFINE. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_SERIAL_NUMBER_VALID"></a><a id="changer_serial_number_valid"></a>CHANGER_SERIAL_NUMBER_VALID

<dd>
<p>The serial number reported by GetProductData is valid and unique for all changers of this type. Serial numbers are not guaranteed to be unique across vendor and product lines. If the changer's serial number is unique according to this definition, the miniclass driver should set this flag and set SerialNumber in CHANGER_PRODUCT_DATA to the serial number.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_PREMOUNT_EJECT_REQUIRED"></a><a id="changer_premount_eject_required"></a>CHANGER_PREMOUNT_EJECT_REQUIRED

<dd>
<p>The changer requires an explicit command issued through a mass storage driver to eject a drive mechanism before the changer can move media from a slot to the drive. For example, a changer with CD-ROM drives might require the tray to be presented to the robotic transport so a piece of media could be loaded onto the tray during a mount operation. If the changer ejects the mechanism automatically, the miniclass driver should clear this flag.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_DEVICE_REINITIALIZE_CAPABLE"></a><a id="changer_device_reinitialize_capable"></a>CHANGER_DEVICE_REINITIALIZE_CAPABLE

<dd>
<p>The changer can recalibrate its transport element in response to an explicit command. The changer class driver calls <b>ChangerReinitializeUnit</b> to initiate recalibration.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_KEYPAD_ENABLE_DISABLE"></a><a id="changer_keypad_enable_disable"></a>CHANGER_KEYPAD_ENABLE_DISABLE

<dd>
<p>The changer keypad can be enabled and disabled programmatically. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_RESERVED_BIT"></a><a id="changer_reserved_bit"></a>CHANGER_RESERVED_BIT

<dd>
<p>Reserved to indicate <b>Features1</b> flags.</p>
</dd>
</dl>
</dd>

### -field <b>Features1</b>

<dd>
<p>Indicates additional features supported by the changer. This member can have one or more of the following values bitwise ORed together.</p>
<p></p>
<dl>

### -field <a id="CHANGER_PREDISMOUNT_ALIGN_TO_SLOT"></a><a id="changer_predismount_align_to_slot"></a>CHANGER_PREDISMOUNT_ALIGN_TO_SLOT

<dd>
<p>Indicates that the transport must be moved to the destination slot before moving the media from a drive to the slot. The bit CHANGER_PREDISMOUNT_ALIGN_TO_DRIVE must be reset if this is set.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_PREDISMOUNT_ALIGN_TO_DRIVE"></a><a id="changer_predismount_align_to_drive"></a>CHANGER_PREDISMOUNT_ALIGN_TO_DRIVE

<dd>
<p>Indicates that the transport must be moved to the drive before moving media from the drive to a slot. The bit CHANGER_PREDISMOUNT_ALIGN_TO_SLOT must be reset if this is set.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_CLEANER_AUTODISMOUNT"></a><a id="changer_cleaner_autodismount"></a>CHANGER_CLEANER_AUTODISMOUNT

<dd>
<p>Indicates that the changer will move the cleaning cartridge back to its original slot automatically, after cleaning is finished. This bit can only be set if CHANGER_DRIVE_CLEANING_REQUIRED is set and CHANGER_CLEANER_OPS_NOT_SUPPORTED is reset. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_TRUE_EXCHANGE_CAPABLE"></a><a id="changer_true_exchange_capable"></a>CHANGER_TRUE_EXCHANGE_CAPABLE

<dd>
<p>Device can manipulate two volumes at a time without using additional changer elements. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_SLOTS_USE_TRAYS"></a><a id="changer_slots_use_trays"></a>CHANGER_SLOTS_USE_TRAYS

<dd>
<p>The changer uses removable trays in its slots, which require the media to be placed in a tray and the tray moved to the desired position.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_RTN_MEDIA_TO_ORIGINAL_ADDR"></a><a id="changer_rtn_media_to_original_addr"></a>CHANGER_RTN_MEDIA_TO_ORIGINAL_ADDR

<dd>
<p>Indicates that when moving volume from drive to slot, volume must go back into the same slot from which it was previously moved to the drive. </p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_CLEANER_OPS_NOT_SUPPORTED"></a><a id="changer_cleaner_ops_not_supported"></a>CHANGER_CLEANER_OPS_NOT_SUPPORTED

<dd>
<p>Indicates that the changer's transport cannot be programmatically commanded by software above the changer driver to move a cleaning cartridge to a dirty drive. This bit can be set only if the CHANGER_DRIVE_CLEANING_REQUIRED bit is set. If this bit is set then both CHANGER_CLEANER_AUTODISMOUNT and CHANGER_CLEANER_SLOT must be reset.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_IEPORT_USER_CONTROL_OPEN"></a><a id="changer_ieport_user_control_open"></a>CHANGER_IEPORT_USER_CONTROL_OPEN

<dd>
<p>The changer requires the user to manually open a closed IEport.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_IEPORT_USER_CONTROL_CLOSE"></a><a id="changer_ieport_user_control_close"></a>CHANGER_IEPORT_USER_CONTROL_CLOSE

<dd>
<p>The changer requires the user to manually close an open IEport.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_MOVE_EXTENDS_IEPORT"></a><a id="changer_move_extends_ieport"></a>CHANGER_MOVE_EXTENDS_IEPORT

<dd>
<p>The changer will extend the tray automatically whenever a command is issued to move media to an IEport.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_MOVE_RETRACTS_IEPORT"></a><a id="changer_move_retracts_ieport"></a>CHANGER_MOVE_RETRACTS_IEPORT

<dd>
<p>The changer will retract the tray automatically whenever a command is issued to move media from an IEport.</p>
</dd>
</dl>
</dd>

### -field <b>MoveFromTransport</b>

<dd>
<p>Indicates whether the changer supports moving a piece of media from a transport element to another transport element, a storage slot, an IEport, or a drive. For a SCSI changer, this is defined in the device capabilities page. The transport is not typically the source or destination for moving or exchanging media. </p>
<dl>
<dd>
<p>Callers can use the following masks to determine whether the changer can move media to a given element.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_TO_TRANSPORT"></a><a id="changer_to_transport"></a>CHANGER_TO_TRANSPORT

<dd>
<p>The changer can carry out the operation from the specified element to a transport.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_TO_SLOT"></a><a id="changer_to_slot"></a>CHANGER_TO_SLOT

<dd>
<p>The changer can carry out the operation from the specified element to a storage slot.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_TO_IEPORT"></a><a id="changer_to_ieport"></a>CHANGER_TO_IEPORT

<dd>
<p>The changer can carry out the operation from the specified element to an IEport.</p>
</dd>
</dl>
<p></p>
<dl>

### -field <a id="CHANGER_TO_DRIVE"></a><a id="changer_to_drive"></a>CHANGER_TO_DRIVE

<dd>
<p>The changer can carry out the operation from the specified element to a drive.</p>
</dd>
</dl>
</dd>

### -field <b>MoveFromSlot</b>

<dd>
<p>Indicates whether the changer supports moving medium from a storage slot to a transport element, another storage slot, an IEport, or a drive. Callers can use the masks described under <b>MoveFromTransport</b> to determine whether the changer supports the move. </p>
</dd>

### -field <b>MoveFromIePort</b>

<dd>
<p>Indicates whether the changer supports moving medium from an IEport to a transport element, a storage slot, another IEport, or a drive. For a SCSI changer, this is defined in the device capabilities page. Callers can use the masks described under <b>MoveFromTransport</b> to determine whether the changer supports the move</p>
</dd>

### -field <b>MoveFromDrive</b>

<dd>
<p>Indicates whether the changer supports moving medium from a drive to a transport element, a storage slot, an IEport, or another drive. Callers can use the masks described under <b>MoveFromTransport</b> to determine whether the changer supports the move. </p>
</dd>

### -field <b>ExchangeFromTransport</b>

<dd>
<p>Indicates whether the changer supports exchanging medium between a transport element and another transport element, a storage slot, an IEport, or a drive. Callers can use the masks described under <b>MoveFromTransport</b> to determine whether the changer supports the exchange. </p>
</dd>

### -field <b>ExchangeFromSlot</b>

<dd>
<p>Indicates whether the changer supports exchanging medium between a storage slot and a transport element, another storage slot, an IEport, or a drive. Callers can use the masks described under <b>MoveFromTransport</b> to determine whether the changer supports the exchange. </p>
</dd>

### -field <b>ExchangeFromIePort</b>

<dd>
<p>Indicates whether the changer supports exchanging medium between an IEport and a transport element, a storage slot, another IEport, or a drive. Callers can use the masks described under <b>MoveFromTransport</b> to determine whether the changer supports the exchange. </p>
</dd>

### -field <b>ExchangeFromDrive</b>

<dd>
<p>Indicates whether the changer supports exchanging medium between a drive and a transport element, a storage slot, an IEport, or another drive. Callers can use the masks described under <b>MoveFromTransport</b> to determine whether the changer supports the exchange. </p>
</dd>

### -field <b>LockUnlockCapabilities</b>

<dd>
<p>Indicates which elements of a changer can be locked or unlocked programmatically. This member is valid only if CHANGER_LOCK_UNLOCK is set in <b>Features0</b>. </p>
<p>Callers can use the following masks to determine whether the changer can lock or unlock a particular element.</p>
<p></p>
<dl>

### -field <a id="LOCK_UNLOCK_IEPORT"></a><a id="lock_unlock_ieport"></a>LOCK_UNLOCK_IEPORT

<dd>
<p>The changer can lock or unlock its IEport(s).</p>
</dd>

### -field <a id="LOCK_UNLOCK_DOOR"></a><a id="lock_unlock_door"></a>LOCK_UNLOCK_DOOR

<dd>
<p>The changer can lock or unlock its door.</p>
</dd>

### -field <a id="LOCK_UNLOCK_KEYPAD"></a><a id="lock_unlock_keypad"></a>LOCK_UNLOCK_KEYPAD

<dd>
<p>The changer can lock or unlock its keypad.</p>
</dd>
</dl>
</dd>

### -field <b>PositionCapabilities</b>

<dd>
<p>Indicates the elements to which a changer can position its transport. Callers can use the masks described under <b>MoveFromTransport</b> to determine whether the changer supports positioning the transport to a particular element. This member is valid only if CHANGER_POSITION_TO_ELEMENT is set in <b>Features0</b>. </p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>

## -remarks
<p><b>GET_CHANGER_PARAMETERS</b> contains the parameters of a changer. The changer miniclass driver allocates and fills in this structure when requested by the changer class driver.</p>

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
<a href="..\mcd\nf-mcd-changergetparameters.md">ChangerGetParameters</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20GET_CHANGER_PARAMETERS structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
