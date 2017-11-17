---
UID: NE.minitape._TAPE_STATUS
title: TAPE_STATUS
author: windows-driver-content
description: The TAPE_STATUS enumeration provides a list of the status codes that the tape class driver uses to report the status of a tape device.
old-location: storage\tape_status.htm
ms.assetid: 45e85ad1-5b75-410e-b9dd-061051bbaa74
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: Storage
req.header: minitape.h
req.include-header: Ntddtape.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TAPE_STATUS
req.alt-loc: minitape.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
ms.keywords: EMULATOR_ACCESS_ENTRY, EMULATOR_ACCESS_ENTRY, *PEMULATOR_ACCESS_ENTRY
req.iface: 
---

# TAPE_STATUS enumeration



## -description
<p>The TAPE_STATUS enumeration provides a list of the status codes that the tape class driver uses to report the status of a tape device.</p>


## -syntax

````
typedef enum _TAPE_STATUS { 
  TAPE_STATUS_SEND_SRB_AND_CALLBACK        = 0,
  TAPE_STATUS_CALLBACK                     = 1,
  TAPE_STATUS_CHECK_TEST_UNIT_READY        = 2,
  TAPE_STATUS_SUCCESS                      = 3,
  TAPE_STATUS_INSUFFICIENT_RESOURCES       = 4,
  TAPE_STATUS_NOT_IMPLEMENTED              = 5,
  TAPE_STATUS_INVALID_DEVICE_REQUEST       = 6,
  TAPE_STATUS_INVALID_PARAMETER            = 7,
  TAPE_STATUS_MEDIA_CHANGED                = 8,
  TAPE_STATUS_BUS_RESET                    = 9,
  TAPE_STATUS_SETMARK_DETECTED             = 10,
  TAPE_STATUS_FILEMARK_DETECTED            = 11,
  TAPE_STATUS_BEGINNING_OF_MEDIA           = 12,
  TAPE_STATUS_END_OF_MEDIA                 = 13,
  TAPE_STATUS_BUFFER_OVERFLOW              = 14,
  TAPE_STATUS_NO_DATA_DETECTED             = 15,
  TAPE_STATUS_EOM_OVERFLOW                 = 16,
  TAPE_STATUS_NO_MEDIA                     = 17,
  TAPE_STATUS_IO_DEVICE_ERROR              = 18,
  TAPE_STATUS_UNRECOGNIZED_MEDIA           = 19,
  TAPE_STATUS_DEVICE_NOT_READY             = 20,
  TAPE_STATUS_MEDIA_WRITE_PROTECTED        = 21,
  TAPE_STATUS_DEVICE_DATA_ERROR            = 22,
  TAPE_STATUS_NO_SUCH_DEVICE               = 23,
  TAPE_STATUS_INVALID_BLOCK_LENGTH         = 24,
  TAPE_STATUS_IO_TIMEOUT                   = 25,
  TAPE_STATUS_DEVICE_NOT_CONNECTED         = 26,
  TAPE_STATUS_DATA_OVERRUN                 = 27,
  TAPE_STATUS_DEVICE_BUSY                  = 28,
  TAPE_STATUS_REQUIRES_CLEANING            = 29,
  TAPE_STATUS_CLEANER_CARTRIDGE_INSTALLED  = 30
} TAPE_STATUS, *PTAPE_STATUS;
````


## -enum-fields
<dl>

### -field <a id="TAPE_STATUS_SEND_SRB_AND_CALLBACK"></a><a id="tape_status_send_srb_and_callback"></a><b>TAPE_STATUS_SEND_SRB_AND_CALLBACK</b>

<dd>
<p>Directs the tape class driver to send the SRB to the device. A tape miniclass routine usually returns this status after filling in the SRB passed by the tape class driver. If the operation is successful, the class driver increments a counter called a "call number" and calls the miniclass routine again. If the SRB fails, the class driver might call the miniclass routine again. For more information about how and when tape miniclass drivers should report this status value, see <a href="NULL">Processing Tape Device Control Requests</a>. </p>
</dd>

### -field <a id="TAPE_STATUS_CALLBACK"></a><a id="tape_status_callback"></a><b>TAPE_STATUS_CALLBACK</b>

<dd>
<p>Directs the tape class driver to increment the call number counter without sending an SRB to the device. For more information about how tape miniclass drivers should make use of this status value, see <a href="NULL">Processing Tape Device Control Requests</a>. </p>
</dd>

### -field <a id="TAPE_STATUS_CHECK_TEST_UNIT_READY"></a><a id="tape_status_check_test_unit_ready"></a><b>TAPE_STATUS_CHECK_TEST_UNIT_READY</b>

<dd>
<p>Directs the tape class driver to create an SRB for the TEST UNIT READY command and to send the SRB to the device. </p>
</dd>

### -field <a id="TAPE_STATUS_SUCCESS"></a><a id="tape_status_success"></a><b>TAPE_STATUS_SUCCESS</b>

<dd>
<p>Indicates that the operation was successful. </p>
</dd>

### -field <a id="TAPE_STATUS_INSUFFICIENT_RESOURCES"></a><a id="tape_status_insufficient_resources"></a><b>TAPE_STATUS_INSUFFICIENT_RESOURCES</b>

<dd>
<p>Indicates that there were not enough resources available to the miniclass driver for it to complete the operation. </p>
</dd>

### -field <a id="TAPE_STATUS_NOT_IMPLEMENTED"></a><a id="tape_status_not_implemented"></a><b>TAPE_STATUS_NOT_IMPLEMENTED</b>

<dd>
<p>Indicates that the requested operation is not supported. </p>
</dd>

### -field <a id="TAPE_STATUS_INVALID_DEVICE_REQUEST"></a><a id="tape_status_invalid_device_request"></a><b>TAPE_STATUS_INVALID_DEVICE_REQUEST</b>

<dd>
<p>Indicates that the requested operation is invalid. </p>
</dd>

### -field <a id="TAPE_STATUS_INVALID_PARAMETER"></a><a id="tape_status_invalid_parameter"></a><b>TAPE_STATUS_INVALID_PARAMETER</b>

<dd>
<p>Indicates that one or more of the parameter values provided with the request are invalid. </p>
</dd>

### -field <a id="TAPE_STATUS_MEDIA_CHANGED"></a><a id="tape_status_media_changed"></a><b>TAPE_STATUS_MEDIA_CHANGED</b>

<dd>
<p>Indicates that the media in the drive might have changed. </p>
</dd>

### -field <a id="TAPE_STATUS_BUS_RESET"></a><a id="tape_status_bus_reset"></a><b>TAPE_STATUS_BUS_RESET</b>

<dd>
<p>Indicates that the bus has been reset. </p>
</dd>

### -field <a id="TAPE_STATUS_SETMARK_DETECTED"></a><a id="tape_status_setmark_detected"></a><b>TAPE_STATUS_SETMARK_DETECTED</b>

<dd>
<p>Indicates that a setmark was encountered during a tape operation. </p>
</dd>

### -field <a id="TAPE_STATUS_FILEMARK_DETECTED"></a><a id="tape_status_filemark_detected"></a><b>TAPE_STATUS_FILEMARK_DETECTED</b>

<dd>
<p>Indicates that a filemark was encountered during a tape operation. </p>
</dd>

### -field <a id="TAPE_STATUS_BEGINNING_OF_MEDIA"></a><a id="tape_status_beginning_of_media"></a><b>TAPE_STATUS_BEGINNING_OF_MEDIA</b>

<dd>
<p>Indicates that the beginning of the media was encountered during a tape operation. </p>
</dd>

### -field <a id="TAPE_STATUS_END_OF_MEDIA"></a><a id="tape_status_end_of_media"></a><b>TAPE_STATUS_END_OF_MEDIA</b>

<dd>
<p>Indicates that the end of the media was encountered during a tape operation. </p>
</dd>

### -field <a id="TAPE_STATUS_BUFFER_OVERFLOW"></a><a id="tape_status_buffer_overflow"></a><b>TAPE_STATUS_BUFFER_OVERFLOW</b>

<dd>
<p>Indicates that a buffer overflow occurred. </p>
</dd>

### -field <a id="TAPE_STATUS_NO_DATA_DETECTED"></a><a id="tape_status_no_data_detected"></a><b>TAPE_STATUS_NO_DATA_DETECTED</b>

<dd>
<p>Indicates that no data was detected. </p>
</dd>

### -field <a id="TAPE_STATUS_EOM_OVERFLOW"></a><a id="tape_status_eom_overflow"></a><b>TAPE_STATUS_EOM_OVERFLOW</b>

<dd>
<p>Indicates that an attempt was made to exceed the physical end of the media during a tape operation. </p>
</dd>

### -field <a id="TAPE_STATUS_NO_MEDIA"></a><a id="tape_status_no_media"></a><b>TAPE_STATUS_NO_MEDIA</b>

<dd>
<p>Indicates that the tape operation failed, because there is no media in the drive. </p>
</dd>

### -field <a id="TAPE_STATUS_IO_DEVICE_ERROR"></a><a id="tape_status_io_device_error"></a><b>TAPE_STATUS_IO_DEVICE_ERROR</b>

<dd>
<p>Indicates that an I/O error occurred during a tape operation. </p>
</dd>

### -field <a id="TAPE_STATUS_UNRECOGNIZED_MEDIA"></a><a id="tape_status_unrecognized_media"></a><b>TAPE_STATUS_UNRECOGNIZED_MEDIA</b>

<dd>
<p>Indicates that the type of the media is not supported. </p>
</dd>

### -field <a id="TAPE_STATUS_DEVICE_NOT_READY"></a><a id="tape_status_device_not_ready"></a><b>TAPE_STATUS_DEVICE_NOT_READY</b>

<dd>
<p>Indicates that the device is not ready. </p>
</dd>

### -field <a id="TAPE_STATUS_MEDIA_WRITE_PROTECTED"></a><a id="tape_status_media_write_protected"></a><b>TAPE_STATUS_MEDIA_WRITE_PROTECTED</b>

<dd>
<p>Indicates that the media is write protected. </p>
</dd>

### -field <a id="TAPE_STATUS_DEVICE_DATA_ERROR"></a><a id="tape_status_device_data_error"></a><b>TAPE_STATUS_DEVICE_DATA_ERROR</b>

<dd>
<p>Indicates that a cyclic redundancy check (CRC) error occurred. </p>
</dd>

### -field <a id="TAPE_STATUS_NO_SUCH_DEVICE"></a><a id="tape_status_no_such_device"></a><b>TAPE_STATUS_NO_SUCH_DEVICE</b>

<dd>
<p>Indicates that no such device exists. </p>
</dd>

### -field <a id="TAPE_STATUS_INVALID_BLOCK_LENGTH"></a><a id="tape_status_invalid_block_length"></a><b>TAPE_STATUS_INVALID_BLOCK_LENGTH</b>

<dd>
<p>Indicates that the block length is invalid. </p>
</dd>

### -field <a id="TAPE_STATUS_IO_TIMEOUT"></a><a id="tape_status_io_timeout"></a><b>TAPE_STATUS_IO_TIMEOUT</b>

<dd>
<p>Indicates that the I/O operation timed out. </p>
</dd>

### -field <a id="TAPE_STATUS_DEVICE_NOT_CONNECTED"></a><a id="tape_status_device_not_connected"></a><b>TAPE_STATUS_DEVICE_NOT_CONNECTED</b>

<dd>
<p>Indicates that the device is disconnected. </p>
</dd>

### -field <a id="TAPE_STATUS_DATA_OVERRUN"></a><a id="tape_status_data_overrun"></a><b>TAPE_STATUS_DATA_OVERRUN</b>

<dd>
<p>Indicates that the tape operation could not be performed because of a data overrun. </p>
</dd>

### -field <a id="TAPE_STATUS_DEVICE_BUSY"></a><a id="tape_status_device_busy"></a><b>TAPE_STATUS_DEVICE_BUSY</b>

<dd>
<p>Indicates that the tape operation could not be performed, because the device is busy. </p>
</dd>

### -field <a id="TAPE_STATUS_REQUIRES_CLEANING"></a><a id="tape_status_requires_cleaning"></a><b>TAPE_STATUS_REQUIRES_CLEANING</b>

<dd>
<p>Indicates that the tape operation could not be performed because the device requires cleaning. </p>
</dd>

### -field <a id="TAPE_STATUS_CLEANER_CARTRIDGE_INSTALLED"></a><a id="tape_status_cleaner_cartridge_installed"></a><b>TAPE_STATUS_CLEANER_CARTRIDGE_INSTALLED</b>

<dd>
<p>Indicates that the media currently in the drive is a cleaner cartridge. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Minitape.h (include Ntddtape.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560625">IOCTL_TAPE_GET_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20TAPE_STATUS enumeration%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
