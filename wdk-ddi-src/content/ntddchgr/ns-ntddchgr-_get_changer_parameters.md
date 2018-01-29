---
UID : NS:ntddchgr._GET_CHANGER_PARAMETERS
title : _GET_CHANGER_PARAMETERS
author : windows-driver-content
description : Retrieves the characteristics of the changer.
old-location : storage\get_changer_parameters.htm
old-project : storage
ms.assetid : c9a47406-5dd2-4cda-b241-3a439406ac75
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : GET_CHANGER_PARAMETERS, GET_CHANGER_PARAMETERS structure [Storage Devices], storage.get_changer_parameters, structs-changer_5c639124-5fc3-4fe8-8289-3bc8408723e0.xml, ntddchgr/GET_CHANGER_PARAMETERS, PGET_CHANGER_PARAMETERS, _GET_CHANGER_PARAMETERS, PGET_CHANGER_PARAMETERS structure pointer [Storage Devices], ntddchgr/PGET_CHANGER_PARAMETERS, *PGET_CHANGER_PARAMETERS
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : GET_CHANGER_PARAMETERS, *PGET_CHANGER_PARAMETERS
---

# _GET_CHANGER_PARAMETERS structure
Retrieves the characteristics of the changer.

## Syntax
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

## Members


`DriveCleanTimeout`

Indicates twice the maximum number of seconds a cleaning is expected to take. The changer's drives should be cleaned by its cleaner cartridge in half the time specified by <b>DriveCleanTimeout</b>. For example, if a drive is typically cleaned in 300 seconds (5 minutes), <b>DriveCleanTimeout</b> should be set to 600.

`ExchangeFromDrive`

Indicates whether the changer supports exchanging medium between a drive and a transport element, a storage slot, an IEport, or another drive. Callers can use the masks described under <b>MoveFromTransport</b> to determine whether the changer supports the exchange.

`ExchangeFromIePort`

Indicates whether the changer supports exchanging medium between an IEport and a transport element, a storage slot, another IEport, or a drive. Callers can use the masks described under <b>MoveFromTransport</b> to determine whether the changer supports the exchange.

`ExchangeFromSlot`

Indicates whether the changer supports exchanging medium between a storage slot and a transport element, another storage slot, an IEport, or a drive. Callers can use the masks described under <b>MoveFromTransport</b> to determine whether the changer supports the exchange.

`ExchangeFromTransport`

Indicates whether the changer supports exchanging medium between a transport element and another transport element, a storage slot, an IEport, or a drive. Callers can use the masks described under <b>MoveFromTransport</b> to determine whether the changer supports the exchange.

`Features0`

Indicates the features supported by the changer. This member can have one or more of the following values bitwise ORed together.

`Features1`

Indicates additional features supported by the changer. This member can have one or more of the following values bitwise ORed together.

`FirstCleanerSlotAddress`

Indicates the number used by the changer vendor to identify the first (and only) slot address assigned to a drive cleaner cartridge to the end user. This must be the value defined by the vendor in the changer's operators guide. For example, if a changer has 8 slots numbered 1 through 8 and its operator's guide designates slot 8 as the drive cleaner slot, <b>FirstSlotNumber</b> would be 1 and <b>FirstCleanerSlotAddress</b> would be 8. If the same 8 slots were numbered 0 through 7, <b>FirstSlotNumber</b> would be 0 and <b>FirstCleanerSlotAddress</b> would be 7. If <b>NumberCleanerSlots</b> is 0, <b>FirstCleanerSlotAddress</b> must be 0.

`FirstDriveNumber`

Indicates the number used by the changer vendor to identify the first data transfer element (drive) in the changer to the end user. <b>FirstDriveNumber</b> is typically 0 or 1, but it can be the first address in a consecutive range of drive addresses defined by the vendor.

`FirstIEPortNumber`

Indicates the number used by the changer vendor to identify the first (and usually only) IEport in the changer to the end user. <b>FirstIEPortNumber</b> is typically 0 or 1, but it can be the first address in a consecutive range of IEport addresses defined by the vendor. If <b>NumberIEElements</b> is 0, <b>FirstIEPortNumber</b> must also be 0.

`FirstSlotNumber`

Indicates the number used by the changer vendor to identify the first storage element (slot) in the changer to the end user, either by marking a magazine or by defining a slot numbering scheme in the changer's operators guide. <b>FirstSlotNumber</b> is typically 0 or 1, but it can be the first address in a consecutive range of slot addresses defined by the vendor.

`FirstTransportNumber`

Indicates the number used by the changer vendor to identify the first (and usually only) transport element in the changer to the end user. <b>FirstTransportNumber</b> is typically 0 or 1, but it can be the first address in a consecutive range of transport addresses defined by the vendor.

`LockUnlockCapabilities`

Indicates which elements of a changer can be locked or unlocked programmatically. This member is valid only if CHANGER_LOCK_UNLOCK is set in <b>Features0</b>. 

Callers can use the following masks to determine whether the changer can lock or unlock a particular element.

`MagazineSize`

Indicates the number of slots in the removable magazines in the changer. This member is valid only if CHANGER_CARTRIDGE_MAGAZINE is set in <b>Features0</b>.

`MoveFromDrive`

Indicates whether the changer supports moving medium from a drive to a transport element, a storage slot, an IEport, or another drive. Callers can use the masks described under <b>MoveFromTransport</b> to determine whether the changer supports the move.

`MoveFromIePort`

Indicates whether the changer supports moving medium from an IEport to a transport element, a storage slot, another IEport, or a drive. For a SCSI changer, this is defined in the device capabilities page. Callers can use the masks described under <b>MoveFromTransport</b> to determine whether the changer supports the move

`MoveFromSlot`

Indicates whether the changer supports moving medium from a storage slot to a transport element, another storage slot, an IEport, or a drive. Callers can use the masks described under <b>MoveFromTransport</b> to determine whether the changer supports the move.

`MoveFromTransport`

Indicates whether the changer supports moving a piece of media from a transport element to another transport element, a storage slot, an IEport, or a drive. For a SCSI changer, this is defined in the device capabilities page. The transport is not typically the source or destination for moving or exchanging media. 

Callers can use the following masks to determine whether the changer can move media to a given element.

`NumberCleanerSlots`

Indicates the number of storage elements (slots) for cleaner cartridges in the changer. For a SCSI changer, this value is not reported in mode sense data, so the miniclass driver must provide it. The miniclass driver should set <b>NumberCleanerSlots</b> to 1 only if the operator's guide for the changer identifies a specific slot as a cleaner slot. If <b>NumberCleanerSlots</b> is 1, then <b>FirstCleanerSlotAddress</b> indicates the zero-based address of the slot in which a drive cleaner should be inserted. If the changer does not support drive cleaning by programmatically moving the cleaner cartridge from its slot to a drive, the miniclass driver must set <b>NumberCleanerSlots</b> to 0. <b>NumberCleanerSlots</b> must not be greater than 1.

`NumberDataTransferElements`

Indicates the number of data transfer elements (drives) in the changer. For a SCSI changer, this is defined in the element address page. Unlike <b>NumberStorageElements</b>, which indicates the total number of possible slots whether the slots are actually present, <b>NumberDataTransferElements</b> indicates the number of drives that are actually present in the changer.

`NumberIEElements`

Indicates the number of IEport elements the changer has for inserting and ejecting of media. For a SCSI changer, this is defined in the element address page. An IEport element must not be part of the storage element (slot) space, and it must be possible to transport media between the IEport and a slot using a MOVE MEDIUM SCSI command. If the changer has a door and not a true IEport, the miniclass driver must set <b>NumberIEElements</b> to 0.

`NumberOfDoors`

Indicates the number of doors that the changer has. For a SCSI changer, this value is not reported in mode sense data, so the miniclass driver must provide it. A door provides access to all media in the changer at once, unlike an IEport which provides access to one or more, but not all, media. A changer's door can be a physical front door or a single magazine that contains all media. If a changer supports only an IEport for inserting and ejecting media, the <b>NumberOfDoors</b> must be 0.

`NumberStorageElements`

Indicates the number of storage elements (slots) in the changer. For a SCSI changer, this is defined in the element address page. This value represents the maximum number of slots available for this changer, including those in removable magazines, whether the magazines are installed. If <b>NumberCleanerSlots</b> is 1, then <b>NumberStorageElements</b> is 1 less than the maximum number of slots in the changer.

`NumberTransportElements`

Indicates the number of transport elements in the changer. For a SCSI changer, this is defined in the element address page. This value is almost always 1, because most changers have a single transport element, which can have one or two picker mechanisms. A changer that has two picker mechanisms on its transport must not be represented as having two transports, because pickers cannot be addressed individually. High-end media libraries can have dual and multiple transport elements for fault tolerance.

`PositionCapabilities`

Indicates the elements to which a changer can position its transport. Callers can use the masks described under <b>MoveFromTransport</b> to determine whether the changer supports positioning the transport to a particular element. This member is valid only if CHANGER_POSITION_TO_ELEMENT is set in <b>Features0</b>.

`Reserved1`

Reserved for future use.

`Reserved2`

Reserved for future use.

`Size`

The size of this structure in bytes. Set to <b>sizeof</b>(GET_CHANGER_PARAMETERS). In effect, this member indicates the version of this structure being used by the miniclass driver.

## Remarks
<b>GET_CHANGER_PARAMETERS</b> contains the parameters of a changer. The changer miniclass driver allocates and fills in this structure when requested by the changer class driver.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddchgr.h |

## See Also

<a href="..\mcd\nf-mcd-changergetparameters.md">ChangerGetParameters</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20GET_CHANGER_PARAMETERS structure%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>