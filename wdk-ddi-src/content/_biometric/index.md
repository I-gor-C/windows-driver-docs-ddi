# Biometric

Overview of the Biometric technology.

To develop Biometric, you need these headers:

 * [winbio_ioctl.h](..\winbio_ioctl\index.md)
 * [winbio_types.h](..\winbio_types\index.md)



## Structures

| Title   | Description   |
| ---- |:---- |
| [WINBIO_BIR structure](..\winbio_types\ns-winbio-types--winbio-bir.md) | The WINBIO_BIR structure is the root of the BIR (Biometric Information Record). It contains the size and offset of any other data elements in the BIR. |
| [WINBIO_BIR_DATA structure](..\winbio_types\ns-winbio-types--winbio-bir-data.md) | The WINBIO_BIR_DATA structure contains the location and size of a block in a BIR. The offset is measured from the beginning of the WINBIO_BIR structure. |
| [WINBIO_BIR_HEADER structure](..\winbio_types\ns-winbio-types--winbio-bir-header.md) | The WINBIO_BIR_HEADER structure contains the Common Biometric Exchange File Format (CBEFF) Patron Format A information that describes the rest of the BIR. |
| [WINBIO_BLANK_PAYLOAD structure](..\winbio_ioctl\ns-winbio-ioctl--winbio-blank-payload.md) | The IOCTL_BIOMETRIC_RESET and IOCTL_BIOMETRIC_UPDATE_FIRMWARE IOCTLs return the WINBIO_BLANK_PAYLOAD structure as output. |
| [WINBIO_CALIBRATION_INFO structure](..\winbio_ioctl\ns-winbio-ioctl--winbio-calibration-info.md) | The IOCTL_BIOMETRIC_CALIBRATE IOCTL returns the WINBIO_CALIBRATION_INFO structure as output. |
| [WINBIO_CAPTURE_DATA structure](..\winbio_ioctl\ns-winbio-ioctl--winbio-capture-data.md) | The IOCTL_BIOMETRIC_CAPTURE_DATA IOCTL returns the WINBIO_CAPTURE_DATA structure as output. |
| [WINBIO_CAPTURE_PARAMETERS structure](..\winbio_ioctl\ns-winbio-ioctl--winbio-capture-parameters.md) | The IOCTL_BIOMETRIC_CAPTURE_DATA IOCTL uses the WINBIO_CAPTURE_PARAMETERS structure as input. |
| [WINBIO_DATA structure](..\winbio_ioctl\ns-winbio-ioctl--winbio-data.md) | The WINBIO_DATA structure specifies data in IOCTL payloads. |
| [WINBIO_DIAGNOSTICS structure](..\winbio_ioctl\ns-winbio-ioctl--winbio-diagnostics.md) | The IOCTL_BIOMETRIC_GET_SENSOR_STATUS IOCTL returns the WINBIO_DIAGNOSTICS structure as output. |
| [WINBIO_GET_INDICATOR structure](..\winbio_ioctl\ns-winbio-ioctl--winbio-get-indicator.md) | The WINBIO_GET_INDICATOR structure is the OUT payload for IOCTL_BIOMETRIC_GET_INDICATOR. |
| [WINBIO_REGISTERED_FORMAT structure](..\winbio_types\ns-winbio-types--winbio-registered-format.md) | The WINBIO_REGISTERED_FORMAT structure specifies a biometric data format. |
| [WINBIO_SENSOR_ATTRIBUTES structure](..\winbio_ioctl\ns-winbio-ioctl--winbio-sensor-attributes.md) | The IOCTL_BIOMETRIC_GET_ATTRIBUTES structure returns the WINBIO_SENSOR_ATTRIBUTES structure as output. |
| [WINBIO_SET_INDICATOR structure](..\winbio_ioctl\ns-winbio-ioctl--winbio-set-indicator.md) | The WINBIO_SET_INDICATOR structure is the IN payload for IOCTL_BIOMETRIC_SET_INDICATOR. |
| [WINBIO_SUPPORTED_ALGORITHMS structure](..\winbio_ioctl\ns-winbio-ioctl--winbio-supported-algorithms.md) | The WINBIO_SUPPORTED_ALGORITHMS structure is the OUT payload for IOCTL_BIOMETRIC_GET_SUPPORTED_ALGORITHMS. |
| [WINBIO_UPDATE_FIRMWARE structure](..\winbio_ioctl\ns-winbio-ioctl--winbio-update-firmware.md) | The WINBIO_UPDATE_FIRMWARE structure is the IN payload for IOCTL_BIOMETRIC_UPDATE_FIRMWARE. |
| [WINBIO_VERSION structure](..\winbio_types\ns-winbio-types--winbio-version.md) | The WINBIO_VERSION structure describes major and minor version information for a WBDI driver. |
